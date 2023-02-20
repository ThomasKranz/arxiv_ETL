from collections import Counter
import pandas as pd

def transform(new_subjects):
    list_keys = list(Counter(new_subjects).keys())
    list_values = list(Counter(new_subjects).values())

    df_keys = pd.DataFrame(list_keys, columns=['subject'])
    df_values = pd.DataFrame(list_values, columns=['frequency'])

    df_arxiv = pd.concat([df_keys, df_values], axis=1)
    df_arxiv['frequency'] = pd.to_numeric(df_arxiv['frequency'])
    df_arxiv = df_arxiv.sort_values(by=['frequency'], ascending=False)

    return df_arxiv
