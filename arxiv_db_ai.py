from src.dbmaker import makedb
from src.visualizer import visualize
from src.transformer import transform
from src.scraper import scrape
from src.reader import read
from src.concator import concate
import os.path
from pathlib import Path


### Extract new subfields of paper submissions

website_url = 'https://arxiv.org/list/cs.AI/pastweek?show=203'
new_subjects = scrape(website_url)

### Transform lists of new submissions into dataframe

df_arxiv = transform(new_subjects)

### Visualize and store data into csv, database

if Path('./data/subject_ai.csv').is_file():
    
    df_csv = read()
   
    df_add_subfields = concate(df_csv, df_arxiv)
    fig = visualize(df_add_subfields)
    df_add_subfields.to_csv('./data/subject_ai.csv', index=False)
    c = makedb(df_add_subfields)
else:
    fig = visualize(df_arxiv)
    df_arxiv.to_csv('./data/subject_ai.csv', index=False)
    c = makedb(df_arxiv)
