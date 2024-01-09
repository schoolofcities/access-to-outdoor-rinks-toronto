<script>

	import TopSofC from "../lib/TopSofC.svelte";
	import HexAccessMap from "../lib/HexAccessMap.svelte";

	import "../assets/global-styles.css";
	import topImage from '../assets/top-image.png';
	import BarGraph from '../lib/bar.svelte'
	import Legend from "../lib/Legend.svelte";
	import ChoroplethMap from "../lib/ChoroplethMap.svelte";
	import VoronoiMap from "../lib/VoronoiMap.svelte";
	import Clustered_bar from "../lib/clustered_bar.svelte";
	import LegendCb from "../lib/LegendCB.svelte";
	
</script>

<TopSofC/>

<main>
	<div class="topImg" style="background-image: url({topImage});">
		
	</div>
	
	<div class="text">
		<div class="title">
			<h1>The Geography of Toronto's Outdoor Skating Rinks</h1>
			<p>Teresa Lau & Jeff Allen // January 2024</p>
		</div>
		<p>
			Cities with colder climates, like many in Canada, ....

			- Why skating rinks are important, cite 2-4 pieces of key literature/new articles
		</p>
		<p>
			- Briefly on history of skating rinks in Toronto, how many are there? what do they offer 
		</p>
		
		<p>
			There are also a number of indoor skating rinks in Toronto, but most of these only have limited public skating hours, typically do not have public ice hockey times, and usually require a small fee for entrance. The outdoor rinks operated by the City are free, and at most times of day are available for leisure skating or ice hockey (the latter is typically scheduled based on age group). The <a href="https://www.toronto.ca/explore-enjoy/recreation/skating-winter-sports/public-leisure-skating">City's website </a> lists the schedules and details for each rink.
		</p>
		<p>
			While there are over 50 outdoor rinks in Toronto, there are large swaths of the City that do not live close to a rink and thus have to travel long distances to access them.
		</p>
		<p>
			Below we've created a map showing the locations of outdoor skating rinks, with the background of the map coloured by the travel time in each neighbourhood to the nearest skating rink. This is a type of <a href="https://en.wikipedia.org/wiki/Isochrone_map">isochrone map</a>, and it highlights which parts of the City have better or worse accessibility to outdoor skating rinks. The map also has a toggle for switching between travel times by walking and by transit.
		</p>

		<br>

		<Legend/>

		<p>
			<span class="bold">Travel Mode:</span>
		</p>

	</div>

	<HexAccessMap/> 

	<div class="text">

		<p>
			Describe pattern on map above here.
		</p>
		
		<p>
			The majority of the former City of Toronto being within a 30 minute walk to the nearest outdoor rink. Conversely, most Scarborough neighbourhoods do not have access to a nearby outdoor rink.
		</p>


		<h2>Who has access?</h2>
	   
		<p>
			Are differences among demographic groups in ability to access to outdoor rinks. Below we create four maps, comparing data from the 2021 Canadian census to the location of outdoor skating rinks. The first map shows population density. This highlights how some of the most-dense neighbourhoods have rinks nearby, but several nodes of high density in the inner-suburbs do not.
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


	<div class="text">
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
		
	</div>

	<div class="text">

		<h2>Catchment Areas</h2>

		<p>
			The City can also be mapped into zones . These are often calle . 
		</p>

		

		
	</div>

	<VoronoiMap/>

	
	<div class="text">

		<h2>Data & Methods</h2>

		<p>
			Describe such here..
		</p>

	</div>

</main>

<style>
	
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
		margin-bottom: 5px;
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

