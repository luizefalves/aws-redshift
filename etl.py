import configparser
import psycopg2
from queries import copy_table_queries, insert_table_queries


''' 
Esse modulo carrega dados da S3 para as staging tables
e  das staging tables para tabelas analíticas.
'''

def load_staging_tables(cur, conn):
    for query in copy_table_queries:  # copy_table_queries = [staging_events_copy, staging_songs_copy]
        cur.execute(query)
        conn.commit()


def insert_tables(cur, conn):
    for query in insert_table_queries:
        cur.execute(query)
        conn.commit()


def main():
    config = configparser.ConfigParser()
    config.read('dwh.cfg')

    conn = psycopg2.connect("host={} dbname={} user={} password={} port={}".format(*config['CLUSTER'].values()))
    cur = conn.cursor()

    load_staging_tables(cur, conn)
    insert_tables(cur, conn)

    conn.close()


if __name__ == "__main__":
    main()