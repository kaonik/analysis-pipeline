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

    def remove_duplicates(self, columns=None):
        """Drop duplicate rows in the DataFrame"""
        self.df.drop_duplicates(subset=columns, inplace=True)
        return self.df

    
    # --- Data Type Conversions ---
    def convert_to_datetime(self, columns):
        """Convert columns to datetime format"""
        for col in columns:
            self.df[col] = pd.to_datetime(self.df[col], errors='coerce')
        return self.df
    
    def convert_to_numeric(self, columns):
        """Convert columns to numeric format"""
        for col in columns:
            self.df[col] = pd.to_numeric(self.df[col], errors='coerce')
        return self.df
    
    def convert_to_categorical(self, columns):
        """Convert columns to categorical format"""
        for col in columns:
            self.df[col] = self.df[col].astype('category')
        return self.df
    
    # --- Handle Outliers ---
    def _calculate_iqr_bounds(self, column):
        """Calculate the lower and upper bounds for outliers"""
        q1 = self.df[column].quantile(0.25)
        q3 = self.df[column].quantile(0.75)
        iqr = q3 - q1
        lower_bound = q1 - 1.5 * iqr
        upper_bound = q3 + 1.5 * iqr
        return lower_bound, upper_bound
    
    def print_outliers_iqr(self, columns):
        """Print outliers in specified columns using IQR method"""
        outliers = {}
        # Calculate lower and upper bounds for each column
        for col in columns:
            lower_bound, upper_bound = self._calculate_iqr_bounds(col)
            outliers_in_col = self.df[(self.df[col] < lower_bound) | (self.df[col] > upper_bound)]
            # Add outliers to dictionary
            if not outliers_in_col.empty:
                outliers[col] = outliers_in_col
        # Print outliers
        for col, outliers_in_col in outliers.items():
            print(f'Outliers in {col}:')
            print(outliers_in_col)