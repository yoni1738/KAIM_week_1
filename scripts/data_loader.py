import pandas as pd

def load_stock_data(file_path):

    return pd.read_csv(file_path, parse_dates=["Date"])
