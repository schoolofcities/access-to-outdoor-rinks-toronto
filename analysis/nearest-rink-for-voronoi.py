import pandas as pd

df = pd.read_csv("data/travel_time/tt_matrix_walk.csv")

df = df.dropna()

min_travel_time_indices = df.groupby('to_id')['travel_time'].idxmin()

final_df = df.loc[min_travel_time_indices]

final_df.reset_index(drop=True, inplace=True)

final_df[["from_id","to_id","travel_time"]].to_csv("data/travel_time/nearest-rink.csv", index = False)

