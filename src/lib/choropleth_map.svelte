<script context="module">
    export const router = true
</script>

<script>
    import { onMount } from 'svelte';
    import * as d3 from 'd3'
    import { geoPath, geoMercator, scaleThreshold } from "d3"; 
    import ctData from "../assets/sm_maps_clean.geo.json" //the census data by CT
    
    var colours = ["#ede9fe", "#dad9f9", "#aaacd4", "#6e6d9f", "#383669"] //colours for the map


    let divWidth = 400;
	$: innerWidth = divWidth;
	$: height = (innerWidth * 40) / 80;

	$: projection = geoMercator()
		.center([-78.17 - 0.0023*innerWidth + 0.000001125*innerWidth**2, 43.5 + 0.00045*innerWidth - 2.5e-7*innerWidth**2])
		.scale([76000 * innerWidth / 800])
		.angle([-17]);
	$: path = geoPath(projection);

</script>