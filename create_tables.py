import configparser
import psycopg2
from queries import create_table_queries, drop_table_queries


def drop_tables(cur, conn):
    for query in drop_table_queries:
        print('Executing drop: '+query)
        cur.execute(query)
        conn.commit()


def create_tables(cur, conn):
    for query in create_table_queries:
        print('Executing create: '+query)
        cur.execute(query)
        conn.commit()


def main():
    config = configparser.ConfigParser()
    config.read('dwh.cfg')
    print('Conectando ao Redshift')
    print(list(config['CLUSTER'].values()))
    conn = psycopg2.connect("host={} dbname={} user={} password={} port={}".format(*config['CLUSTER'].values()), connect_timeout=20)
    cur = conn.cursor()
    print('Conexão Estabelecida')

    drop_tables(cur, conn)
    print('Criando Tabelas...')
    create_tables(cur, conn)

    conn.close()


if __name__ == "__main__":
    main()