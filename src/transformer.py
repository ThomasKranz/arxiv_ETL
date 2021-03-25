from collections import Counter
import pandas as pd

def transform(new_subjects):
    list1 = list(Counter(new_subjects).keys())
    list2 = list(Counter(new_subjects).values())
    df1 = pd.DataFrame(list1, columns=['subject'])
    df2 = pd.DataFrame(list2, columns=['frequency'])
    df3 = pd.concat([df1, df2], axis=1)
    df3['frequency'] = pd.to_numeric(df3['frequency'])
    df3 = df3.sort_values(by=['frequency'], ascending=False)
    return df3

