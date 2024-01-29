import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def basic_data_exploration(df):
    '''Perform basic data exploration on a DataFrame'''

    print('Dataset Overview')
    print('----------------')
    print(f'Shape: {df.shape}')
    print('\nData Types:')
    print(df.dtypes)
    print('\nMissing Values:')
    print(df.isnull().sum())
    print('\nDuplicate Rows:', df.duplicated().sum())

    print('\nStatistical Summary (Numerical Data)')
    print('------------------------------------')
    print(df.describe())

    print('\nStatistical Summary (Categorical Data)')
    print('--------------------------------------')
    if df.select_dtypes('object').empty:
        print('No categorical data')

    else:
        for col in df.select_dtypes(include='object').columns:
            print(f'\nColumn: {col}')
            print(df[col].value_counts())
    

    # Correlation Matrix and Histograms for numerical data
    numerical_cols = df.select_dtypes(include=[float,int])
    if not numerical_cols.empty:
        print('\nCorrelation Matrix')
        print('------------------')
        print(numerical_cols.corr())
        
        print('\nVisual Exploration')
        print('------------------')

        for col in numerical_cols.columns:
                fig, axes = plt.subplots(1, 2, figsize=(10, 5))

                axes[0].hist(df[col])
                axes[0].set_title(f'{col} Histogram')

                sns.boxplot(y=df[col], ax=axes[1])
                axes[1].set_title(f'{col} Boxplot')

                plt.tight_layout()
                plt.show()

    else:
        print('No numerical data for correlation matrix or histograms')

    print('\nEnd of Exploration')
    print('------------------')
