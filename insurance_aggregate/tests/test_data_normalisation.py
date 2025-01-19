import pytest
import pandas as pd
from data_normalisation import normalise_data

def test_normalise_broker1_data():
    data = pd.DataFrame({
        'PolicyNumber': ['POL001'],
        'InsuredAmount': [1000000],
        'StartDate': ['15/01/2023'],
        'EndDate': ['15/01/2024'],
        'ClientRef': ['CR001']
    })
    normalized_data = normalise_data(data, 'broker1')
    assert 'policy_number' in normalized_data.columns
    assert 'insured_amount' in normalized_data.columns
    assert normalized_data['insured_amount'][0] == 1000000

def test_normalise_broker2_data():
    data = pd.DataFrame({
        'PolicyRef': ['POL040'],
        'CoverageAmount': [550000],
        'InitiationDate': ['20/03/2026'],
        'ExpirationDate': ['20/03/2027'],
        'ConsumerID': ['CID01']
    })
    normalized_data = normalise_data(data, 'broker2')
    assert 'policy_number' in normalized_data.columns
    assert 'insured_amount' in normalized_data.columns
    assert normalized_data['insured_amount'][0] == 550000

def test_normalise_invalid_source():
    data = pd.DataFrame()
    with pytest.raises(ValueError):
        normalise_data(data, 'unknown_broker')
