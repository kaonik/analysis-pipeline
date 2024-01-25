import pandas as pd
import unittest
from src.data_ingestion import load_csv

#Change working directory to the directory of the current file
import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))

class TestDataIngestion(unittest.TestCase):

    def test_load_csv_valid(self):
        '''Test loading a valid csv file'''
        df = load_csv('../data/realtor-data.csv')
        self.assertIsInstance(df, pd.DataFrame) # check if df is a pandas dataframe

    def test_load_csv_invalid(self):
        '''Test loading an invalid (non existent) csv file'''
        df = load_csv('data/non_existent.csv')
        self.assertIsNone(df) # check if df is None

if __name__ == '__main__':
    unittest.main()
