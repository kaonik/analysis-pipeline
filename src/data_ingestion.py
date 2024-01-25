import pandas as pd

def load_csv(file_path):
    """Load csv file into a pandas dataframe"""
    try:
        return pd.read_csv(file_path)
    except FileNotFoundError:
        print("File not found")
        return None