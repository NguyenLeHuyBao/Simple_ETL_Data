from config.dev import PostgresSource
from db_handler.postgres_handler import PostgresHandler
from db_handler.queries import PostgresStatements
import pandas as pd


def ingest_psql_source(**kwargs):
    postgres_handler = PostgresHandler(
        PostgresSource.HOST,
        PostgresSource.PORT,
        PostgresSource.USER,
        PostgresSource.PASSWORD,
        PostgresSource.DATABASE
    )

    for index, table in enumerate(PostgresStatements.list_tables):
        sql_query = PostgresStatements.list_queries[index]
        list_columns = PostgresStatements.list_columns[index]

        print('Start getting data from source Postgres - Table:', table)
        data = postgres_handler.action_db(query_str=sql_query, action='select')
        print('Found {0} records need to be inserted'.format(len(data)))
        df = pd.DataFrame(data, columns=list_columns)
        df['location'] = 'ThaiLand'

        print('Start ingesting data from source Postgres to DW - Table:', table)
        postgres_handler.action_db(action='insert', data=df, table=table)
        print('Finished ingesting data from source to DW - Table:', table)
