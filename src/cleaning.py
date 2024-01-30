import pandas as pd

class DataCleaner:
    def __init__(self, df):
        """Initialize with a DataFrame"""
        self.df = df

    # --- Handle Missing Data ---
    def drop_missing_rows(self):
        """Drop rows with missing values"""
        self.df.dropna(inplace=True)
        return self.df

    def drop_missing_columns(self, threshold=0.5):
        """Drop columns with missing values above a specified threshold"""
        self.df.dropna(thresh=threshold*len(self.df), axis=1, inplace=True)
        return self.df
    
    def fill_missing_values(self, columns, strategy='mean'):
        """Impute missing values in specified columns using specified strategy"""
        for col in columns:
            if strategy == 'mean':
                self.df[col].fillna(self.df[col].mean(), inplace=True)
            elif strategy == 'median':
                self.df[col].fillna(self.df[col].median(), inplace=True)
            elif strategy == 'mode':
                self.df[col].fillna(self.df[col].mode()[0], inplace=True)
            else:
                print('Invalid imputation strategy')
                return None
        return self.df
    
    # --- Dealing with Duplicates ---
    def print_duplicate_rows(self, columns=None, max_print_rows=100):
        """Print or write duplicate rows in the DataFrame to a file"""
        duplicates = self.df[self.df.duplicated(subset=columns)]
        if not duplicates.empty:
            if duplicates.shape[0] <= max_print_rows:
                print('Duplicate Rows:')
                print(duplicates)
            else:
                duplicates.to_csv('duplicates.csv', index=False)
                print(f'Duplicate rows written to duplicates.csv')
        else:
            print('No duplicate rows found')

    def drop_duplicate_rows(self, columns=None):
        """Drop duplicate rows in the DataFrame"""
        self.df.drop_duplicates(subset=columns, inplace=True)
        return self.df

    