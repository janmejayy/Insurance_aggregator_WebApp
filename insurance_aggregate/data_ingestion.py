
import pandas as pd
import os

def load_data(file_path):
    try:
        # Check file existence and format
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"File not found: {file_path}")
        if not file_path.endswith('.csv'):
            raise ValueError(f"Unsupported file format: {file_path}. Only CSV files are supported.")
        
        # Load data and drop columns with null values
        data = pd.read_csv(file_path)
        data = data.dropna(axis=1, how='any')  # Drop columns with any null values
        return data
    except Exception as e:
        raise ValueError(f"Error loading data from {file_path}: {e}")
