<script>

    import TopSofC from "../lib/TopSofC.svelte";
    import HexAccessMap from "../lib/HexAccessMap.svelte";

    import "../assets/global-styles.css";
    import topImage from '../assets/top-image.png';
    import BarGraph from '../lib/bar.svelte'
    import Legend from "../lib/Legend.svelte";
    import ChoroplethMap from "../lib/choropleth_map.svelte";
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
            <p>Jeff Allen & Teresa Lau - November 2023</p>
        </div>
        <p>
            Cities with colder climates, like many in Canada, 

            - Why skating rinks are important, cite 2-4 pieces of key literature/new articles
            - Briefly on history of skating rinks in Toronto, how many are there? what do they offer (public skating/hockey/classes/can be booked for activities)
        </p>
        <p>
            While there are over 50 outdoor rinks in Toronto, there are large swaths of the City that do not live close to a rink and thus have to travel long distances to access them.
        </p>
        <p>
            Below we've created a map showing the locations of outdoor skating rinks, with the background coloured by the travel time in each neighbourhood to the nearest skating rink. This is a type of <a href="">isochrone map</a>. 
        </p>

    </div>

    <HexAccessMap/> 

    <div class="text">
        <Legend/>
        <p>
            Briefly describe map here, patterns, etc.
        </p>


        <h2>Who has access?</h2>
       
        <p>
            Describe ...
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
            <BarGraph/>
        </p>
        
        <p>
            Describe bar graph......
        </p>

        <p>
            <Clustered_bar/>
            <LegendCb/>
        </p>
        
    </div>

</main>

<style>
.mapGrid {
    margin: auto;
    padding-bottom: 42px;
    max-width: 1200px;
    width: 100%;
    display: grid;
    gap: 4px 2px;
    grid-template-columns: repeat(2, 1fr);
}

@media (max-width:900px) {
    .mapGrid {
        grid-template-columns: repeat(1, 1fr);
        /* gap: 0px 0px; */
        /* width: calc(100% - 40px); */
    }
}

.mapSmall {
    /* background-color: #3d53fb; */
    /* z-index: -10; */
    margin: auto;
    padding: -10px;
    max-width: 600px;
    width: 600px;
    margin: 0 auto;
    /* border: solid 1px #f4f4f4; */
}

</style>

