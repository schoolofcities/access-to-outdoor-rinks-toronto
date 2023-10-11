# #Create network dataset and calculate travel time
# set_env JAVA_HOME=C:\Program Files\Microsoft\jdk-17.0.8.101-hotspot\

import geopandas as gpd
import pandas as pd
import numpy as np
import fiona
import r5py
import datetime

#Bring in the geojson files for rinks and hex_grid
rinks = gpd.read_file("analysis/data/rinks.geojson")
#Data must contain an ID column
rinks["id"] = rinks._id

hex_grid = gpd.read_file("analysis/data/hex-grid-centroids.geojson")

#Create transport network
transport_network = r5py.TransportNetwork("data/osm/Toronto.osm.pbf",["data/TTC/gtfs.zip"])

#Compute travel time matrix for walking and transit on a weekday at 6:30pm
from r5py import TransportMode
travel_time_matrix_computer = r5py.TravelTimeMatrixComputer(
    transport_network,origins=rinks,destinations=hex_grid,
    departure=datetime.datetime(2023,9,6,18,30), 
    transport_modes=[TransportMode.WALK, TransportMode.TRANSIT], speed_walking=4.5)
#Build travel time matrix (for each hex to each ring)
travel_time_matrix = travel_time_matrix_computer.compute_travel_times()
travel_time_matrix.to_csv("data/travel_time/tt_matrix.csv", index = True)
#fill na values to 120 min max
tt = pd.read_csv("data/travel_time/tt_matrix.csv")
tt["travel_time"] = tt["travel_time"].fillna(120)
#Find minimum walking + transit time from hex to the cloest ring
min_tt_wt_630 = tt.groupby("to_id").agg({"travel_time":[min]})
min_tt_wt_630 = min_tt_wt_630.rename(columns ={"travel_time":"walk_&_transit_weekday"}) #rename column name
min_tt_wt_630.to_csv("data/travel_time/access-min-travel-time.csv")

#Compute travel time matrix for walking
from r5py import TransportMode
travel_time_matrix_computer_walk = r5py.TravelTimeMatrixComputer(
    transport_network,origins=rinks,destinations=hex_grid,
    departure=datetime.datetime(2023,9,6,18,30),
    transport_modes=[TransportMode.WALK], speed_walking=4.5)
#Build travel time matrix - walking (for each hex to each ring)
travel_time_matrix_walk = travel_time_matrix_computer_walk.compute_travel_times()
travel_time_matrix_walk.to_csv("data/travel_time/tt_matrix_walk.csv", index = True)
#fill na values to 120 min max
tt_walk = pd.read_csv("data/travel_time/tt_matrix_walk.csv")
tt_walk["travel_time"] = tt_walk["travel_time"].fillna(120)
#Find minimum walking time from hex to the cloest ring
min_tt_walk = tt_walk.groupby("to_id").agg({"travel_time":[min]})
min_tt_walk = min_tt_walk.rename(columns ={"travel_time":"walk"}) #remane column name
min_tt_walk.to_csv("data/travel_time/min_walking_travel_time")


#Compute travel time matrix for transit ONLY on a weekday at 6:30pm
travel_time_matrix_computer_transit_weekday = r5py.TravelTimeMatrixComputer(
    transport_network,origins=rinks,destinations=hex_grid,
    departure=datetime.datetime(2023,9,6,18,30),
    transport_modes=[TransportMode.TRANSIT], speed_walking=4.5)
#Build travel time matrix - transit on a weekday (for each hex to each ring)
travel_time_matrix_computer_transit_weekday = travel_time_matrix_computer_transit_weekday.compute_travel_times()
travel_time_matrix_computer_transit_weekday.to_csv("data/travel_time/tt_matrix_transit_weekday", index = True)
#fill na values to 120 min max
tt_transit_weekday = pd.read_csv("data/travel_time/tt_matrix_transit_weekday")
tt_transit_weekday["travel_time"] = tt_transit_weekday["travel_time"].fillna(120)
#Find minimum transit time from hex to the cloest ring on a weekday
min_tt_transit_weekday = tt_transit_weekday.groupby("to_id").agg({"travel_time":[min]})
min_tt_transit_weekday = min_tt_transit_weekday.rename(columns = {"travel_time":"transit_weekday"}) #rename column
min_tt_transit_weekday.to_csv("data/travel_time/min_transit_travel_time")


#Compute travel time matrix for transit on a weekend at 2:30pm
travel_time_matrix_computer_transit_weekend = r5py.TravelTimeMatrixComputer(
    transport_network,origins=rinks,destinations=hex_grid,
    departure=datetime.datetime(2023,9,9,14,30), 
    transport_modes=[TransportMode.TRANSIT], speed_walking=4.5)
#Build travel time matrix - transit on a weekend (for each hex to each ring)
travel_time_matrix_computer_transit_weekend = travel_time_matrix_computer_transit_weekend.compute_travel_times()
travel_time_matrix_computer_transit_weekend.to_csv("data/travel_time/tt_matrix_transit_weekend", index = True)
#fill na values to 120 min max
tt_matrix_transit_weekend = pd.read_csv("data/travel_time/tt_matrix_transit_weekend")
tt_matrix_transit_weekend["travel_time"] = tt_matrix_transit_weekend["travel_time"].fillna(120)
#Find minimum transit time from hex to the cloest ring on a weekend
min_tt_transit_weekend = tt_matrix_transit_weekend.groupby("to_id").agg({"travel_time":[min]})
min_tt_transit_weekend = min_tt_transit_weekend.rename(columns = {"travel_time":"transit_weekend"}) #rename column
min_tt_transit_weekend.to_csv("data/travel_time/min_tt_transit_weekend")

#Use inner join to combine all tables into one df
final = pd.concat([min_tt_wt_630,min_tt_walk,min_tt_transit_weekday,min_tt_transit_weekend],
                 axis=1, join="inner").droplevel(1,axis=1).reset_index(drop=False)
#Export final datatable to a csv
final.to_csv("data/travel_time/travel_time_final.csv")

#Previous version of calculating travel time
# import sys
# sys.argv.append(["--max-memory", "16G"])

# # import geopandas as gpd
# import geopandas as gpd
# import r5py
# import datetime

# rinks = gpd.read_file("data/rinks.geojson")

# rinks["id"] = rinks._id

# print(rinks.head(100))

# hex = gpd.read_file("data/hex-grid-centroids.geojson")

# print(hex)

# transport_network = r5py.TransportNetwork(
#     "data/osm/Toronto.osm.pbf",
# )

# travel_time_matrix_computer = r5py.TravelTimeMatrixComputer(
#     transport_network,
#     origins=rinks,
#     destinations=hex,
#     departure=datetime.datetime(2022,2,22,8,30),
#     transport_modes=[r5py.LegMode.WALK]
# )

# travel_time_matrix = travel_time_matrix_computer.compute_travel_times()
# print(travel_time_matrix.head(60))

# travel_time_matrix.to_csv("data/tt_matrix.csv", index=True)