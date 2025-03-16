import pandas as pd

def create_dataframe():
    data = {'Namerr': ['Alice', 'Bob', 'Charlie'], 'Age': [25, 30, 35]}
    df = pd.DataFrame(data)
    return df
