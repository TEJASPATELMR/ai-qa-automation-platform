import pandas as pd

def load_excel_mapping(path):

    df = pd.read_excel(path, engine="openpyxl")

    return df.to_string()