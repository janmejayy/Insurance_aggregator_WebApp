import pandas as pd

def normalise_data(data, source):
    # Mapping column names based on the source
    column_map = {
        'broker1': {
            'PolicyNumber': 'policy_number',
            'InsuredAmount': 'insured_amount',
            'StartDate': 'start_date',
            'EndDate': 'end_date',
            'ClientRef': 'customer'
        },
        'broker2': {
            'PolicyRef': 'policy_number',
            'CoverageAmount': 'insured_amount',
            'InitiationDate': 'start_date',
            'ExpirationDate': 'end_date',
            'ConsumerID': 'customer'
        }
    }.get(source, {})

    if not column_map:
        raise ValueError(f"Unknown source: {source}")

    # Rename columns
    data = data.rename(columns=column_map)

    # Convert date columns to datetime and handle missing values
    for date_column in ['start_date', 'end_date']:
        if date_column in data.columns:
            # Parse dates with explicit `dayfirst=True` to silence warnings
            data[date_column] = pd.to_datetime(data[date_column], errors='coerce', dayfirst=True)

            # Handle missing values
            if date_column == 'start_date':
                # Replace NaT with the earliest valid date or a default fallback
                earliest_date = data[date_column].dropna().min()
                fallback_date = pd.Timestamp('1900-01-01')  # Default fallback
                data[date_column] = data[date_column].fillna(earliest_date if earliest_date else fallback_date)
            elif date_column == 'end_date':
                # Drop rows with missing end_date
                data = data[data[date_column].notna()]

    # Ensure all required columns exist after normalization
    required_columns = list(column_map.values())
    missing_columns = [col for col in required_columns if col not in data.columns]
    if missing_columns:
        raise ValueError(f"Critical columns missing after normalization: {missing_columns}")

    # Ensure data types for numeric columns
    if 'insured_amount' in data.columns:
        data['insured_amount'] = pd.to_numeric(data['insured_amount'], errors='coerce').fillna(0)

    return data
