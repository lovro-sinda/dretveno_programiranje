# Seaborn visualization library
import seaborn as sns
import pandas as pd

tips2 = pd.read_csv('data/main_players.csv')
# Create the default pairplot
sns.pairplot(tips2)
