import pyodbc
import pandas as pd
from sql_queries import *
import numpy as np


def process_data(cur, filepath:str, insert_query):
    
    df = pd.read_csv(filepath, encoding='latin-1')
    df.replace(np.nan, 'NaN', inplace=True)
    
    for index, row in df.iterrows():
        cur.execute(insert_query, list(row))
        
def main():
    
    connection_str = "DRIVER={ODBC Driver 17 for SQL Server};SERVER=localhost;UID=SA;PWD=Goodness15."
    conn = pyodbc.connect(connection_str, autocommit=True)
    cur = conn.cursor()
    cur.execute('USE sales_analysis_project')
    
    data_files = ['Sales Analysis Data/Categories.csv', 'Sales Analysis Data/Customers.csv', 'Sales Analysis Data/Employees.csv', 'Sales Analysis Data/OrderDetails.csv', 'Sales Analysis Data/Orders.csv', 'Sales Analysis Data/Products.csv', 'Sales Analysis Data/Shippers.csv', 'Sales Analysis Data/Suppliers.csv']
    
    for file, insert_query  in zip(data_files, insert_records_queries):
        process_data(cur, file, insert_query)
        
    conn.close()
        
if __name__=='__main__':
    main()
        