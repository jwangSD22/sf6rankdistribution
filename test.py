from data_analysis import makeplot
from datetime import datetime

import boto3

makeplot.output_plots()

bucket_name = 'sf6rankdistribution'
current_date = datetime.now().strftime("%Y-%m-%d")


s3 = boto3.client('s3')

s3.upload_file('current_bar.png', bucket_name, 'current/current_bar.png')
s3.upload_file('current_pie.png', bucket_name, 'current/current_pie.png')
s3.upload_file('rank_distribution.csv', bucket_name, 'current/current_csv.csv')

s3.upload_file('current_bar.png', bucket_name, f'images/bar/{current_date}--bar.png')
s3.upload_file('current_pie.png', bucket_name, f'images/pie/{current_date}--pie.png')

s3.upload_file('rank_distribution.csv', bucket_name, f'csv/{current_date}--csv.csv')
