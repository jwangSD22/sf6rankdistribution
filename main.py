
import pandas as pd
from datetime import datetime

from scraper import scrape

leagues = ['Rookie','Iron','Bronze','Silver','Gold','Platinum','Diamond','Master']

league = []
division = []
players = []


for item in leagues:
    if item != 'Master':
        for _ in range(1,6):
            league.append(item)
            division.append(_)

league.append('Master')
division.append(1)

for index in range(36):
    player_count = scrape(league[index],division[index],index+1)
    players.append(player_count)
    print(f'Finished {league[index]} {division[index]} with {player_count} players.')


dict = {'League':league,'Division':division,'Number of Players':players}
df = pd.DataFrame(dict)

current_date = datetime.now().strftime("%Y-%m-%d")
output_filename =f'{current_date}--rank_distribution.csv'

df.to_csv(output_filename)

# df.to_csv('rank_distribution.csv')



## run jupyter notebooks code here.. 

## output file with date to output folder