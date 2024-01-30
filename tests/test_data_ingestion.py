import pandas as pd
import unittest
import os

import src.data_ingestion as di

#Change working directory to the directory of the current file
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# Environment variables & calls
DB_NAME = os.environ.get('DB_NAME')
DB_USER = os.environ.get('DB_USER')
DB_PASSWORD = os.environ.get('DB_PASSWORD')
DB_HOST = os.environ.get('DB_HOST')
OPENWEATHER_API_KEY = os.environ.get('OPENWEATHER_API_KEY')
query = '''
    select * from Forecast
    limit 1000;
'''
url = f"https://api.openweathermap.org/data/2.5/forecast?lat=0&lon=0&appid={OPENWEATHER_API_KEY}&units=imperial"


class TestCSVIngestion(unittest.TestCase):

    def test_load_csv_valid(self):
        '''Test loading a valid csv file'''
        df = di.load_csv('../data/realtor-data.csv')
        self.assertIsInstance(df, pd.DataFrame) # check if df is a pandas dataframe

    def test_load_csv_invalid(self):
        '''Test loading an invalid (non existent) csv file'''
        df = di.load_csv('data/non_existent.csv')
        self.assertIsNone(df) # check if df is None

class TestPostgresIngestion(unittest.TestCase):

    def test_load_postgres_valid(self):
        '''Test loading data from a valid PostgreSQL database'''
        result = di.load_from_postgres(DB_NAME, DB_USER, DB_PASSWORD, DB_HOST, query)
        self.assertIsInstance(result, pd.DataFrame)

    def test_bad_password(self):
        '''Test with bad password'''
        result = di.load_from_postgres(DB_NAME, DB_USER, 'bad_password', DB_HOST, query)
        self.assertIsNone(result)

    def test_bad_query(self):
        '''Test with bad query'''
        result = di.load_from_postgres(DB_NAME, DB_USER, DB_PASSWORD, DB_HOST, 'bad_query')
        self.assertIsNone(result)

    def test_bad_host(self):
        '''Test with bad host'''
        result = di.load_from_postgres(DB_NAME, DB_USER, DB_PASSWORD, 'bad_host', query)
        self.assertIsNone(result)

    def test_bad_dbname(self):
        '''Test with bad dbname'''
        result = di.load_from_postgres('bad_dbname', DB_USER, DB_PASSWORD, DB_HOST, query)
        self.assertIsNone(result)

    def test_bad_user(self):
        '''Test with bad user'''
        result = di.load_from_postgres(DB_NAME, 'bad_user', DB_PASSWORD, DB_HOST, query)
        self.assertIsNone(result)


class TestAPIIngestion(unittest.TestCase):

    def test_load_api_valid(self):
        '''Test loading data from a valid API'''
        result = di.load_from_api(url)
        self.assertIsInstance(result, dict)

    def test_load_api_invalid(self):
        '''Test loading data from an invalid API'''
        result = di.load_from_api('https://api.openweathermap.org/data/2.5/forecast?lat=0&lon=0&appid=bad_api_key&units=imperial')
        self.assertIsNone(result)

if __name__ == '__main__':
    unittest.main()
