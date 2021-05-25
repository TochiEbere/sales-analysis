import pyodbc
from sql_queries import *


def create_database(db_name:str):
    
    """
    Create a database and connect to it
    """
    
    connection_str = "DRIVER={ODBC Driver 17 for SQL Server};SERVER=localhost;UID=SA;PWD=Goodness15."
    conn = pyodbc.connect(connection_str, autocommit=True)
    
    cur = conn.cursor()
    
    query_DB_drop = f'DROP DATABASE IF EXISTS {db_name}'
    query_DB_create = f'CREATE DATABASE {db_name}'
    
    cur.execute(query_DB_drop)
    cur.execute(query_DB_create)
    
    cur.execute(f'USE {db_name}')
    
    
    return conn, cur


def drop_tables(cur):
    """
    Drop tables if exists using the drop_tables query list
    """
    
    for query in drop_tables_queries:
        cur.execute(query)
        
def create_tables(cur):
    """
    Create tables using the create_tables query list
    """
    
    for query in create_tables_queries:
        cur.execute(query)
    
    
def main():
    
    conn, cur = create_database('sales_analysis_project')
    drop_tables(cur)
    create_tables(cur)
    
    conn.close()
    

if __name__=='__main__':
    main()