import unittest
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

import src.basic_exploration as be

class TestBasicDataExploration(unittest.TestCase):

    def setUp(self):
        # Create a sample DataFrame for testing
        self.df = pd.DataFrame({
            'A': [1, 2, 3, 4, 5],
            'B': ['a', 'b', 'c', 'd', 'e'],
            'C': [1.1, 2.2, 3.3, 4.4, 5.5]
        })

    def test_basic_data_exploration_valid(self):
        '''Test basic data exploration on a valid DataFrame'''
        be.basic_data_exploration(self.df)

    def test_basic_data_exploration_not_dataframe(self):
        '''Test basic data exploration with a non-DataFrame input'''
        result = be.basic_data_exploration('not_a_dataframe')
        self.assertIsNone(result)

    def test_basic_data_exploration_empty_dataframe(self):
        '''Test basic data exploration with an empty DataFrame'''
        empty_df = pd.DataFrame()
        result = be.basic_data_exploration(empty_df)
        self.assertIsNone(result)

    def test_basic_data_exploration_categorical_data(self):
        '''Test basic data exploration with categorical data'''
        df_with_categorical = pd.DataFrame({
            'A': [1, 2, 3, 4, 5],
            'B': ['a', 'b', 'c', 'c', 'a'],
            'C': [1.1, 2.2, 3.3, 4.4, 5.5]
        })
        be.basic_data_exploration(df_with_categorical)

    def test_basic_data_exploration_no_categorical_data(self):
        '''Test basic data exploration with no categorical data'''
        df_no_categorical = pd.DataFrame({
            'A': [1, 2, 3, 4, 5],
            'B': [1, 2, 3, 4, 5],
            'C': [1.1, 2.2, 3.3, 4.4, 5.5]
        })
        be.basic_data_exploration(df_no_categorical)

    def test_basic_data_exploration_numerical_data(self):
        '''Test basic data exploration with numerical data'''
        be.basic_data_exploration(self.df)

    def test_basic_data_exploration_no_numerical_data(self):
        '''Test basic data exploration with no numerical data'''
        df_no_numerical = pd.DataFrame({
            'A': ['a', 'b', 'c', 'd', 'e'],
            'B': ['a', 'b', 'c', 'd', 'e'],
            'C': ['a', 'b', 'c', 'd', 'e']
        })
        be.basic_data_exploration(df_no_numerical)

if __name__ == '__main__':
    unittest.main()