<script>

	import TopSofC from "../lib/TopSofC.svelte";
	import HexAccessMap from "../lib/HexAccessMap.svelte";

	import "../assets/global-styles.css";
	import topImage from '../assets/top-image.png';
	import Legend from "../lib/Legend.svelte";
	import ChoroplethMap from "../lib/ChoroplethMap.svelte";
	import VoronoiMap from "../lib/VoronoiMap.svelte";
	
</script>

<TopSofC/>

<main>
	<div class="topImg" style="background-image: url({topImage});">
		
	</div>
	
	<div class="text">
		<div class="title">
			<h1>The Geography of Toronto's Outdoor Skating Rinks</h1>
			<p>Jeff Allen & Teresa Lau /// January 2024</p>
		</div>
		<p>
			Outdoor skating rinks in cities with colder climates, like many cities in Canada, are important pieces of civic infrastructure in communities. They provide residents the opportunity to affordably partake in outdoor physical activity and <a href="https://www.cogitatiopress.com/urbanplanning/article/view/3430">social interaction</a>, particularly on winter days when other types of outdoor activities are limited due to low temperatures or snowfall.
		</p>
		<p>
			The City of Toronto has long operated publicly accessible outdoor skating rinks. Currently there are 54 City operated artificial ice rinks located in public parks, as well as a few independently operated outdoor rinks. Many of the City operated rinks have have boards and are used both for leisure skating and ice hockey (i.e. shinny); some rinks are skating trails which are only used for leisure skating; while some sites have both a rink with boards and a skating pad or trail used for leisure skating. The City operated rinks are free, and at most times of day are available for leisure skating or ice hockey (the latter is typically scheduled based on age group). The <a href="https://www.toronto.ca/explore-enjoy/recreation/skating-winter-sports/public-leisure-skating">City of Toronto's website</a> lists the schedules and details for each rink.
		</p>
		<p>
			Outdoor skating rinks in Toronto are quite popular, evidenced by <a href="https://www.cbc.ca/news/canada/toronto/reservations-toronto-artificial-ice-rinks-pandemic-lockdown-exercise-1.5826289">thousands of online reservations</a> due to limited spots during the COVID-19 pandemic and public backlash when a <a href="https://toronto.citynews.ca/2022/01/22/community-rallies-to-try-and-save-west-end-skating-rink/">rink closes</a>. Since they're free to use, they are generally an affordable option for winter activity (outside of the costs of buying or renting skates). Outdoor rinks also do no go unused during the warmer months; those with boards are often home to activities like lacrosse, pickle ball, and cycle polo, while skating trails are often used for roller skating or skateboarding.
		</p>
		<p>
			While there are over 50 outdoor rinks in Toronto, there are large swaths of the City that do not live close to a rink and thus have to travel long distances to access them. To investigate how this varies across the City we've created a map showing the locations of outdoor skating rinks in Toronto, with the background of the map coloured by the travel time in each neighbourhood to the nearest outdoor skating rink. This is a type of <a href="https://en.wikipedia.org/wiki/Isochrone_map">isochrone map</a>, and it highlights which parts of the City have better or worse accessibility to outdoor skating rinks. 
		</p>
		<p>
			The map has a toggle for switching between travel times by walking and by transit. Clicking on a rink will show a popup displaying the name of the rink.
		</p>

		<div class="breakline"></div>

		<Legend/>

		<p>
			<span class="bold">Travel Mode:</span>
		</p>

	</div>

	<HexAccessMap/> 

	<div class="text">
		
		<p>
			Overall we can see substantial differences in proximity to outdoor rinks across the City. Almost all of the former City of Toronto is within a 30 minute walk to the nearest outdoor rink. Conversely, residents in many Scarborough neighbourhoods have to travel further to access outdoor rinks. Etobicoke, on the other hand, has a greater number of outdoor rinks, most built prior to amalgamation in the late 90s.
		</p>
		<p>
			Note that there are also a number of indoor skating rinks in Toronto, but we don't include them on this map, since indoor rinks have far less public skating hours and typically do not have public ice hockey times. They usually require a small fee for entrance. Skating indoors is also a different experience than outdoors. Part of the a attraction of outdoor skating rinks is doing something outside during the winter.
		</p>

		<h2>Who has access?</h2>
	   
		<p>
			Transportation researchers, such as the those part of the <a href="https://mobilizingjustice.ca/">Mobilizing Justice</a> partnership, are increasingly calling for identifying and remediating inequalities in accessibility to important destinations and services, particularly if inequalities exist among equity seeking groups like low-income households and recent immigrants.
		</p>
		<p>
			Below we create four maps, comparing demographic data from the <a href="https://www12.statcan.gc.ca/census-recensement/2021/dp-pd/prof/index.cfm?Lang=E">2021 Canadian Census</a> to the location of outdoor skating rinks. The first map shows population density. This highlights how some of the most-dense neighbourhoods have rinks nearby, but several nodes of high density in the inner-suburbs do not. The next three maps compare the location of outdoor rinks to three demographic groups; low-income residents, visible minorities, and immigrants. Each of these maps is coloured by the percent in each group relative to the overall population in the neighbourhood. We find that immigrants and visibile minorities have worse accessibility to outdoor rinks relative to the overall population, party due to higher proportions in the inner-suburb Scarborough. The average travel time to the nearest rink for each demographic group is displayed below each map.
		</p>
	</div>

	<div class="mapGrid">
		<div class="mapSmall">
			<ChoroplethMap demoGP="PopDen"/>
		</div>
		<div class="mapSmall">
			<ChoroplethMap demoGP="Immi%"/>
		</div>
		<div class="mapSmall">
			<ChoroplethMap demoGP="VM%"/>
		</div>
		<div class="mapSmall">
			<ChoroplethMap demoGP="LIn%"/>
		</div>
	</div>

	<!-- <div class="text">
		<p>
			Describe maps
		</p>
				
		<p>
			Describe bar graph......
		</p>

		<p>
			<Clustered_bar/>
			<LegendCb/>
		</p>
	</div> -->

	<div class="text">

		<h2>Catchment Areas</h2>

		<p>
			Another way of looking at the geographic variations in the location of skating rinks is to map how many people each skating rink serves. The City of Toronto's <a href="https://www.toronto.ca/city-government/accountability-operations-customer-service/long-term-vision-plans-and-strategies/parks-and-recreation-facilities-master-plan/">Parks & Recreation Facilities Master Plan</a> states that there should be at least one outdoor skating rink per 100,000 residents. At over 50 rinks and a population of just over 3 million, the City is currently meeting it's internally defined goal. However, the picture is different when mapping the <a href="https://en.wikipedia.org/wiki/Catchment_area">catchment area</a> of each rink, and counting the population that resides in each one.
		</p>
		<p>
			Check out the map below. We generated this from the travel times shown on the map at the top of this page, grouping the city into areas based on their nearest outdoor skating rink. This is a type of <a href="https://en.wikipedia.org/wiki/Voronoi_diagram">Voronoi diagram</a> that in this case is derived by shortest walking time. For areas that are more than a 60 minute walk to a rink, we deem as inaccessible, and are coloured in grey. By counting the population in each catchment area, we can map how many residents each rink serves, assuming residents would usually skate at the rink nearest to them.
		</p>

		<VoronoiMap/>

		<p>
			The darkest areas on the map indicate outdoor rinks that serve a large population. As the City continues to grow in population, it would be prudent to site any new outdoor skating rinks within these areas that currently have lower levels of access and are above the 100,000 residents per rink threshold. This would reduce existing inequalities in proximity to outdoor skating rinks, as well as even out the distribution of rinks which will help the City adequately meet it's internal planning goals.
		</p>

	</div>

	<div class="notes">

		<h2>Data & Methods</h2>

		<p>
			We created the isochrone map showing travel time to the nearest rink by 1) genearting a hexagonal grid (using <a href="https://qgis.org/en/site/">QGIS</a>) covering the City of Toronto, then 2) using network analysis software, <a href="https://github.com/r5py/r5py">R5Py</a>, to compute the travel time from each grid, and then 3) visualizing the minimum travel time for each hexagonal grid cell. The travel times for walking were derived from <a href="https://www.openstreetmap.org">OpenStreetMap</a> network data. The public transit travel times are based on <a href="https://open.toronto.ca/dataset/ttc-routes-and-schedules/">transit schedule data</a> (in GTFS format). The travel times by public transit were calculated for a typical weekday at 6pm and a Saturday at 2pm (two times we think residents are most likely to travel to rinks). The results were very similar so we averaged the two results into a single transit metric.
		</p>
		<p>
			The demographic data are from the <a href="https://www12.statcan.gc.ca/census-recensement/2021/dp-pd/prof/index.cfm?Lang=E">2021 Canadian census</a>. They are mapped at the census tract geography, which roughly correspond to neighbourhoods.
		</p>
		<p>
			This webpage was built using the JavaScript framework <a href="https://svelte.dev/">Svelte</a>, with help from <a href="https://d3js.org/">D3</a> and <a href="https://maplibre.org/">MapLibre GL JS</a> to create the maps.
		</p>
		<p>
			Data and code for this work are on <a href="https://github.com/schoolofcities/access-to-outdoor-rinks-toronto">GitHub</a>.
		</p>

	</div>

</main>

<style>

	.breakline {
		width: 100%;
		border-top: solid 1px var(--brandLightBlue);
		height: 15px;
	}
	
    /* Default styles for the container and divs */
    .mapGrid {
		margin: 0 auto;
		display: flex;
		flex-wrap: wrap;
		justify-content: space-around;
		max-width: 1201px;
    }

    .mapSmall {
		width: 100%; /* Default to 100% width */
		box-sizing: border-box;
		margin-bottom: 40px;
		border-top: solid 1px var(--brandLightBlue);
		border-bottom: solid 1px var(--brandLightBlue);
    }

    /* Media query for screens with a width greater than 1200px */
    @media (min-width: 1201px) {
      .mapSmall {
        width: 48%; /* Display 2x2 at 1200px and wider */
      }
    }

    /* Media query for screens between 600px and 1200px */
    @media (min-width: 601px) and (max-width: 1200px) {
      .mapSmall {
        width: 580px; /* Display exactly 600px wide */
      }
    }

    /* Media query for screens less than 600px */
    @media (max-width: 600px) {
      .mapSmall {
        width: 100%; /* Adjust to screen width */
        min-width: 400px; /* Set a minimum width */
      }
    }



</style>

