import pandas as pd
import os

script_directory = os.path.dirname(os.path.abspath(__file__))
output_relative_path = 'output/'
output_path = os.path.join(script_directory, output_relative_path, 'output.csv')



data = {
    'Name': ['John', 'Alice', 'Bob', 'Charlie'],
    'Age': [28, 24, 22, 30],
    'City': ['New York', 'San Francisco', 'Los Angeles', 'Chicago']
}

df = pd.DataFrame(data)

df.to_csv(output_path, index=False)
