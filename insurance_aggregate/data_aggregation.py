
import pandas as pd

def aggregate_data(data_list):
    combined_data = pd.concat(data_list, ignore_index=True)
    return combined_data
