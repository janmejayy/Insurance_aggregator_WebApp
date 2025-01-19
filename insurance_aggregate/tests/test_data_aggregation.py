import pandas as pd
from data_aggregation import aggregate_data

def test_aggregate_data():
    broker1_data = pd.DataFrame({
        'policy_number': ['POL001'],
        'insured_amount': [1000000],
        'customer': ['CR001']
    })
    broker2_data = pd.DataFrame({
        'policy_number': ['POL002'],
        'insured_amount': [750000],
        'customer': ['CID01']
    })
    aggregated_data = aggregate_data([broker1_data, broker2_data])
    assert len(aggregated_data) == 2
    assert 'policy_number' in aggregated_data.columns
