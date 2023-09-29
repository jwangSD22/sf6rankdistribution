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

print(league)
print(division)
print((len(league),len(division)))