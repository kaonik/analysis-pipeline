import pandas as pd
import psycopg2

def load_csv(file_path):
    """Load csv file into a pandas dataframe"""
    try:
        return pd.read_csv(file_path)
    except FileNotFoundError:
        print("File not found")
        return None
    
def load_from_postgres(dbname, user, password, host, port, query):
    ''' Load data from postgres database into a pandas dataframe'''
    try:
        with psycopg2.connect(dbname=dbname, user=user, password=password, host=host, port=port) as conn:
            return pd.read_sql_query(query, conn)
    except psycopg2.Error as e:
        print(f'Database error: {e}')
        return None