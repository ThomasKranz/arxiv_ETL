import pandas as pd

def concate(df_arxiv, df_csv):
    df_add_subfields = pd.concat([df_csv, df_arxiv]).groupby('subject').sum().sort_values(
        by=['frequency'], ascending=False).reset_index()

    return df_add_subfields
