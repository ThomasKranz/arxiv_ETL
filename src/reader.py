import pandas as pd

def read():
    df_csv = pd.read_csv('./data/subject_ai.csv')
    
    return df_csv
