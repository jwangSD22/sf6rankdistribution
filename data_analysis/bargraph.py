import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

color_gradients = [
    # Rookie (Purple Theme)
    '#D0D0FF', '#ADADFF', '#8585FF', '#5C5CFF', '#3333FF',

    # Iron
    '#E5E5E5', '#BFBFBF', '#999999', '#737373', '#4D4D4D',

    # Bronze (Darker Brown)
    '#8B4513', '#7A3C12', '#693411', '#582C10', '#47240F',

    # Silver
    '#CCCCCC', '#A6A6A6', '#808080', '#595959', '#333333',

    # Gold
    '#FFD700', '#FFC100', '#FFAB00', '#FF9500', '#FF8000',

    # Platinum
    '#99CC99', '#88BB88', '#77AA77', '#669966', '#558855',

    # Diamond
    '#00BFFF', '#00AEEF', '#00A1DF', '#0093CE', '#0086BE',

    # Master (Deeper Red)
    '#800000'
]

plt.figure(figsize=(10,10))

data = pd.read_csv('../rank_distribution.csv')

league = data['League'].to_numpy()
division = data['Division'].astype(str).to_numpy()
league_combined = league+' '+division+' '


x = league_combined
y = data['Number of Players']

plt.xticks(rotation=90)
plt.bar(x,y,color=color_gradients)

plt.savefig('test.png',dpi=300)


plt.show()

