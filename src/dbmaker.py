from pathlib import Path
import sqlite3

def makedb(df_add_subfields):
    Path('./data/subjects.db').touch()
    conn = sqlite3.connect('./data/subjects.db')
    c = conn.cursor()
    df_add_subfields.to_sql('counts_ai', conn, if_exists='replace', index=False)

    return c
