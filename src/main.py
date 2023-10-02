
import pandas as pd
import time
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
    # time.sleep(10)
    player_count = scrape(league[index],division[index],index+1)
    players.append(player_count)
    print(f'Finished {league[index]} {division[index]} with {player_count} players.')


time.sleep(3)

dict = {'League':league,'Division':division,'Number of Players':players}

df = pd.DataFrame(dict)

print(df)

df.to_csv('rank_distribution.csv')