import matplotlib.pyplot as plt
from matplotlib import rcParams
from pathlib import Path
import seaborn as sns
import matplotlib.style as style
import matplotlib.patches as patches

def visualize(df_add_subfields):
    style.use('fivethirtyeight')
    fig, ax = plt.subplots(figsize=(25, 20))
    sns.barplot(x=df_add_subfields['frequency'], y=df_add_subfields.loc[:29, 'subject'], ax=ax, palette='mako', alpha=0.75).set_title(
        '\nTop 30 related subfields of AI measured by submissions of scientific papers since February 2021 at arxiv.org\n')
    ax.set(xlabel='frequencies of submissions of papers', ylabel='subfields of AI')

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
