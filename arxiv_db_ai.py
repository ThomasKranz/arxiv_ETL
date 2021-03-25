from src.dbmaker import makedb
from src.visualizer import visualize
from src.transformer import transform
from src.scraper import scrape
import os.path
from pathlib import Path

### Extract

website_url = 'https://arxiv.org/list/cs.AI/pastweek?show=203'
new_subjects = []
scrape(website_url, new_subjects)

### Transform

df3 = transform(new_subjects)

### Load

if Path('./data/subject_ai.csv').is_file():
    from src.reader import read
    df4 = read()
    from src.concator import concate
    df_add = concate(df4, df3)
    fig = visualize(df_add)
    df_add.to_csv('./data/subject_ai.csv', index=False)
    c = makedb(df_add)
else:
    fig = visualize(df3)
    df3.to_csv('./data/subject_ai.csv', index=False)
    c = makedb(df3)
print(c.execute('''SELECT * FROM counts_ai LIMIT 5''').fetchall())
