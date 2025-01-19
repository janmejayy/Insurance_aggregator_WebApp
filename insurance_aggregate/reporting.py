import pandas as pd

def calculate_metrics(data):
    # Calculate metrics based on cleaned data
    active_policies = data[
        (data['start_date'] <= pd.Timestamp.now()) &
        (data['end_date'] > pd.Timestamp.now())
    ]
    metrics = {
        'total_policies': len(data),
        'unique_customers': data['customer'].nunique(),
        'sum_insured_amount': data['insured_amount'].sum(),
        # Round average policy duration to two decimal places
        'average_policy_duration': round(
            active_policies.apply(
                lambda row: (row['end_date'] - row['start_date']).days, axis=1
            ).mean(), 2
        ) if not active_policies.empty else 0
    }
    return metrics


def filter_by_broker(data, broker_name):
    """
    Filters the policies based on the broker name.

    Parameters:
    - data (DataFrame): The dataset containing policies.
    - broker_name (str): The name of the broker to filter.

    Returns:
    - DataFrame: Filtered policies for the specified broker.
    """
    return data[data['broker'].str.contains(broker_name, case=False, na=False)]
