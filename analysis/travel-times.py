import sys
sys.argv.append(["--max-memory", "16G"])

# import geopandas as gpd
import geopandas as gpd
import r5py
import datetime

rinks = gpd.read_file("data/rinks.geojson")

rinks["id"] = rinks._id

print(rinks.head(100))

hex = gpd.read_file("data/hex-grid-centroids.geojson")

print(hex)

transport_network = r5py.TransportNetwork(
    "data/osm/Toronto.osm.pbf",
)

travel_time_matrix_computer = r5py.TravelTimeMatrixComputer(
    transport_network,
    origins=rinks,
    destinations=hex,
    departure=datetime.datetime(2022,2,22,8,30),
    transport_modes=[r5py.LegMode.WALK]
)

travel_time_matrix = travel_time_matrix_computer.compute_travel_times()
print(travel_time_matrix.head(60))

travel_time_matrix.to_csv("data/tt_matrix.csv", index=True)
