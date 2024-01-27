import pandas as pd
from sqlalchemy import create_engine
import requests

def load_csv(file_path):
    """Load csv file into a pandas dataframe"""
    try:
        return pd.read_csv(file_path)
    except FileNotFoundError:
        print("File not found")
        return None
    
def load_from_postgres(dbname, user, password, host, query, port=5432):
    """Load data from a PostgreSQL database using SQLAlchemy."""
    try:
        # Create an SQLAlchemy engine
        engine = create_engine(f'postgresql://{user}:{password}@{host}:{port}/{dbname}')
        
        # Use the engine to execute the query and load into DataFrame
        with engine.connect() as conn:
            return pd.read_sql_query(query, conn)
    except Exception as e:
        print(f"Database error: {e}")
        return None
    
def load_from_api(url):
    ''' Load data from an API into a pandas dataframe'''
    try:
        response = requests.get(url)
        response.raise_for_status() # Raise HTTPError for bad requests
        return response.json() # Return json response
    except requests.RequestException as e:
        print(f'Request error: {e}')
        return None