import matplotlib.pyplot as plt
from matplotlib import rcParams
from pathlib import Path
import seaborn as sns
import matplotlib.style as style
import matplotlib.patches as patches

def visualize(df_add):
    style.use('fivethirtyeight')
    fig, ax = plt.subplots(figsize=(20, 7))
    sns.barplot(x=df_add['frequency'], y=df_add.loc[:10, 'subject'].drop([1], axis=0), ax=ax, palette='mako', alpha=0.75).set_title(
        'Most related subfields of AI measured by submissions of scientific papers in 2021')
    ax.set(xlabel='submissions of papers', ylabel='subfields of AI')
    for p in ax.patches:
        height = p.get_height()
        width = p.get_width()
        ax.text(x=width+3,
                y=p.get_y()+(height/2),
                s='{: .0f}'.format(width), fontweight='bold')
    ax.set_xticks(ax.get_xticks()[::1])
    plt.show()
    plt.tight_layout()
    fig = plt.gcf()
    fig.savefig('./results/subject_ai-viz.png')
