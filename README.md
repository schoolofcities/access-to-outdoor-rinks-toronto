

# Access to outdoor skating rinks Toronto

Analyze and map the inequalities of spatial access to outdoor skating rinks in Toronto, by walking and by public transit.

The analysis will be similar to this [previous work](https://findingspress.org/article/24072-changes-in-transit-accessibility-to-food-banks-in-toronto-during-covid-19), but focused on rinks instead of food banks, and written in a more publicly accessible language.

The final product will be a blog post/visual essay hosted on the School of Cities website.

Code and analysis should be easy to replicate for other types of destinations - I would like to do a similar story in the spring/early summer on access to outdoor pools




### Currently in the analysis folder ...

'dowonload-osm.py' uses pyrosm to download OSM data for Toronto and saves the .pbf locally

'travel-times.py' computes the travel times, for the specified mode, from all hexagon centroids to all rinks

'access.py' summarize the travel times, by finding the minimum travel time from each hexagon (i.e. each hex is given the shortest duration to reach any rink)



## To do

1) Download latest OSM data - what is currently in the folder is from early 2023

2) Download latest TTC GTFS data from City of Toronto

3) Build a network graph combining 1) and 2) and 

4) Generate travel times and map accessibility (similar to what is currently in `rink-map.qgz`) with this updated data for three scenarios 
    - Walking Only
    - Public Transit, 7pm on a weekday
    - Public Transit, 2pm on a Saturday

5) Download DA-level 2021 census data, link this to hexagons, to then analyze how accessibility varies for different population groups (this will take a bit of thinking on how to automate)

6) Start drafting / creating a blog post - writing content and making pretty figures


## Open Questions

1) How to incorporate, if at all, comparitive analysis for skating only vs skating + hockey rinks

2) How to incorporate, if at all, accounting for rinks that have different operating hours

3) Can / should we look at rink usage statistics (might need a FOI request)



### Notes from earlier
- public hours of rinks vary by rink - account for this somehow
- City's park and rec master plan - https://www.toronto.ca/city-government/accountability-operations-customer-service/long-term-vision-plans-and-strategies/parks-and-recreation-facilities-master-plan/
- map and argue for new rink locations? - portlands / golden mile / etc.
- 100,000 people / outdoor rink - is the city's plan - source?
- FOI - rink usage?
- argmument against rinks - lack of summer activity - but are often used in summer for other activities (pickle ball, lacrosse, basketball, bike polo)
- what is the cost per rink? if new

