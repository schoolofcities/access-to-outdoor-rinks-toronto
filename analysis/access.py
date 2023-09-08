import pandas as pd

df = pd.read_csv("data/tt_matrix.csv")

df['travel_time'] = df['travel_time'].fillna(120)

dfm = df.groupby('to_id').agg({'travel_time': ['min']})

dfm.to_csv("data/access-min-travel-time.csv")