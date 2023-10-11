import pandas as pd
import numpy as np

#Data files are downloaded from Census Mapper with Toronto DAs

#Data file 1 - Median Income
df1 = pd.read_csv("data/census/data.csv")
df1 = df1.set_index(["GeoUID"]).rename(columns={
    "v_CA21_560: Median total income in 2020 among recipients ($)":"Median Income(2020,$)"})

#Data file 2 - Immigrant and visble minority population
df2 = pd.read_csv("data/census/data (2).csv")
#Rename columns and remove duplicate columns 
df2 = df2.set_index(["GeoUID"]).rename(columns={
    "v_CA21_4410: Immigrants":"# of Immigrants",
    "v_CA21_4875: Total visible minority population":"# of Visible Minority"})
df2 = df2.drop(columns=["Type", "Region Name", "Area (sq km)", "Population ", "Dwellings ", "Households "])

#Combine both dfs into one df
census = df1.join(df2, how="left")
census.replace(0, np.nan, inplace=True) #to debug zero float division error

#Calculate immigrant and visible miniority percentages
census["Immigrant%"] = census.apply(lambda x: x["# of Immigrants"]/x["Population "]*100, axis=1)
census["Visible Minority%"] = census.apply(lambda x: x["# of Visible Minority"]/x["Population "]*100, axis =1)

#Calculate population density, immigrant density, visible minority density
census["Population Density"] = census.apply(lambda x: x["Population "]/x["Area (sq km)"], axis =1)
census["Immigrant Density"] = census.apply(lambda x: x["# of Immigrants"]/x["Area (sq km)"], axis =1)
census["Visible Minority Density"]= census.apply(lambda x: x["# of Visible Minority"]/x["Area (sq km)"], axis =1)

#Export as a csv file
census.to_csv("data/census/census.csv")
