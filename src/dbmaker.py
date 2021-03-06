from pathlib import Path
import sqlite3

def makedb(df_add):
    Path('./data/subjects.db').touch()
    conn = sqlite3.connect('./data/subjects.db')
    c = conn.cursor()
    df_add.to_sql('counts_ai', conn, if_exists='replace', index=False)
    return c