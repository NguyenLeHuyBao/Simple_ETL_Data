import psycopg2
import psycopg2.extras as extras
from config.dev import DWHInfo


class PostgresHandler:
    def __init__(self, host, port, username, password, database):
        # Source config
        self.host = host
        self.port = port
        self.username = username
        self.password = password
        self.database = database
        self.schema = 'public'

        # Destination config
        self.destination_host = DWHInfo.HOST
        self.destination_port = DWHInfo.PORT
        self.destination_username = DWHInfo.USER
        self.destination_password = DWHInfo.PASSWORD
        self.destination_database = DWHInfo.DATABASE
        self.destination_schema = 'raw_data'

        self.destination_connection = self._create_destination_conn()
        self.connection = self._create_conn()

    def _create_conn(self):
        conn = psycopg2.connect(
            host=self.host,
            port=self.port,
            user=self.username,
            password=self.password,
            database=self.database,
            options=f'-c search_path={self.schema}'
        )

        return conn

    def _create_destination_conn(self):
        conn = psycopg2.connect(
            database=self.destination_database,
            user=self.destination_username,
            password=self.destination_password,
            host=self.destination_host,
            port=self.destination_port,
            options=f'-c search_path={self.destination_schema}'
        )
        return conn

    def _get_data(self, query_str):
        cur = self.connection.cursor()
        cur.execute(query_str)
        records = cur.fetchall()
        return records

    def _push_data(self, data, table):
        tuples = [tuple(x) for x in data.to_numpy()]

        cols = ','.join(list(data.columns))

        query = "INSERT INTO %s(%s) VALUES %%s" % (table, cols)
        cursor = self.destination_connection.cursor()
        try:
            extras.execute_values(cursor, query, tuples)
            self.destination_connection.commit()
        except (Exception, psycopg2.DatabaseError) as error:
            print("Error: %s" % error)
            self.destination_connection.rollback()
            cursor.close()
            return 1
        print("the dataframe is inserted")
        cursor.close()

    def _change_data(self, query_str):
        cur = self.connection.cursor()
        cur.execute(query_str)
        print('Successfully modified data')

    def action_db(self, query_str=None, action=None, data=None, table=None):
        """
        :param table: table in db to perform action
        :param query_str: string to query
        :param action: select or insert or None
        :param data: if action == Insert then data is DataFrame, else None
        :return: result
        """
        if action == 'select':
            return self._get_data(query_str)
        elif action == 'insert':
            return self._push_data(data, table)
        else:
            return self._change_data(query_str)
