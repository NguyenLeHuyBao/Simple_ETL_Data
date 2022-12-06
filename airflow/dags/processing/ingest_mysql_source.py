from config.dev import MysqlSource
from db_handler.mysql_handler import MysqlHandler
from db_handler.queries import MysqlStatements
import pandas as pd


def ingest_mysql_source(**kwargs):
    mysql_handler = MysqlHandler(
        MysqlSource.HOST,
        MysqlSource.PORT,
        MysqlSource.USER,
        MysqlSource.PASSWORD,
        MysqlSource.DATABASE
    )

    for index, table in enumerate(MysqlStatements.list_tables):
        sql_query = MysqlStatements.list_queries[index]
        list_columns = MysqlStatements.list_columns[index]

        print('Start getting data from source Mysql - Table:', table)
        data = mysql_handler.action_db(query_str=sql_query, action='select')
        print('Found {0} records need to be inserted'.format(len(data)))
        df = pd.DataFrame(data, columns=list_columns)
        df['location'] = 'VietNam'

        print('Start ingesting data from source Mysql to DW - Table:', table)
        mysql_handler.action_db(action='insert', data=df, table=table)
        print('Finished ingesting data from source to DW - Table:', table)
