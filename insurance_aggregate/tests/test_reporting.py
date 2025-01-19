import pandas as pd

def calculate_metrics(data):
    active_policies = data[
        (data['start_date'] <= pd.Timestamp.now()) & (data['end_date'] > pd.Timestamp.now())
    ]
    metrics = {
        'total_policies': len(data),
        'unique_customers': data['customer'].nunique(),
        'sum_insured_amount': data['insured_amount'].sum(),
        'average_policy_duration': active_policies['end_date']
            .sub(active_policies['start_date'])
            .dt.days.mean() if not active_policies.empty else 0
    }
    return metrics
