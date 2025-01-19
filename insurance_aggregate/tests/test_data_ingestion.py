
import pytest
import pandas as pd
import os
from data_ingestion import load_data

def test_load_data_success(monkeypatch):
    # Mock CSV content
    mock_data = pd.DataFrame({
        'PolicyNumber': ['POL001', 'POL002'],
        'InsuredAmount': [1000000, 750000],
        'StartDate': ['15/01/2023', '10/02/2023'],
        'EndDate': ['15/01/2024', '10/02/2024']
    })

    # Mock os.path.exists to always return True
    def mock_exists(file_path):
        return True

    # Mock pandas read_csv to return the mock data
    def mock_read_csv(file_path):
        return mock_data

    monkeypatch.setattr(os.path, 'exists', mock_exists)
    monkeypatch.setattr(pd, 'read_csv', mock_read_csv)

    # Call the function and verify the output
    data = load_data('broker1.csv')
    assert not data.empty
    assert 'PolicyNumber' in data.columns

def test_load_data_file_not_found(monkeypatch):
    # Mock os.path.exists to return False
    def mock_exists(file_path):
        return False

    monkeypatch.setattr(os.path, 'exists', mock_exists)

    # Call the function and expect a ValueError with the correct message
    with pytest.raises(ValueError, match="Error loading data from nonexistent.csv: File not found: nonexistent.csv"):
        load_data('nonexistent.csv')

def test_load_data_unsupported_format():
    # Call the function with an unsupported format and expect a ValueError
    with pytest.raises(ValueError):
        load_data('broker1.json')
