# SF6 Rank Analytics Platform: AWS Web Scraping and Visualization

## Description

- Developed and implemented a Python app using Selenium WebDriver in headless mode for efficient web scraping of gaming data. Processed the acquired data through pandas and Matplotlib within a structured Jupyter Notebook environment.
- Automated the project using a cronjob on a Linux instance deployed on AWS EC2. Leveraged AWS (Lambda and EventBridge) to manage the instance's on/off state, resulting in cost reduction and resource optimization.
- Scheduled and executed monthly transfers of visually compelling data representations to AWS S3, enhancing accessibility and utilization for subsequent projects.



## Technologies Used
- AWS (S3, EC2, Lambda, EventBridge)
- Pandas
- Matplotlib
- Plotly
- Jupyter Notebook
- Selenium
- Python
- Linux (ssh,scp)


## Learning points
- Understanding how SSH works into EC2 instances to work remotely
- Learning how to structure data using Jupyter Notebook to later turn into Python scripts.
- Developing graphs from graphing libraries
- Exploring web scraping using Selenium (cases where BeautifulSoup can not directly access data).
- Setting up cronjobs wthin Linux but also within the AWS environment.
