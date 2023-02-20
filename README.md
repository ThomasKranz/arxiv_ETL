![alt text](https://github.com/ThomasKranz/arxiv_ETL/blob/master/results/subject_ai-viz.png){:target="_blank"}

# arxiv_ETL - CI/CD Pipeline

This repo tries to observe the trend in AI by scraping the subjects of the submitted papers which are related primary to AI. The library used for scraping is beautifulsoup.

Source: https://arxiv.org/list/cs.AI/pastweek?show=155

After extraction the data will be visualized using Matplotlib and seaborn and the visualiszation stored as a .png file.

The data will be finally stored in .csv and .db files using SQlite3.

This repo contains a yaml file in the github folder to run this project as CI/CD pipeline. The workflow is scheduled for one daily run.

The script can also be run as a batch-file. Have a look at the 'Run_python_file.bat'.

Codes are still not commented. Pls contact me for any questions. Enjoy trying it out!
