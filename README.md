# arxiv_ETL - CI/CD Pipeline

This repo observes the trend of A.I. by counting submitted papers which are related primary to A.I. at 

https://arxiv.org/list/cs.AI/pastweek?show=155

After extraction the data will be visualized and stored as a .png file.

The data will be finally stored in .csv and .db files using SQlite3.

This repo contains a yaml file to run this project as CI/CD pipeline. The workflow is scheduled for a daily run at noon.

The visualization below is updated daily.
![alt text](https://github.com/ThomasKranz/arxiv_ETL/blob/master/results/subject_ai-viz.png)

For older versions, pls have a look at the commit history.
