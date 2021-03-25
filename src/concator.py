import pandas as pd

def concate(df3, df4):
    df_add = pd.concat([df4, df3]).groupby('subject').sum().sort_values(
        by=['frequency'], ascending=False).reset_index()
    return df_add
