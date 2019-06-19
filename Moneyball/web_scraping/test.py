import pandas as pd
df = pd.read_csv("dr1.csv")
df['new_column'] = 'some_value'
df.to_csv('dr1.csv')
