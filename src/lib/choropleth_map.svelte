<script>
    import { onMount } from 'svelte';
    import * as d3 from 'd3';
    import { geoPath, geoMercator, scaleThreshold } from "d3"; 
    import ctData from "../assets/ctData.geo.json"; //the census data by CT
    
    var ledColours = ["#ede9fe", "#dad9f9", "#aaacd4", "#6e6d9f", "#383669"] //colours for the map

    export let demoGP;
    
    const demoGPs = {
        "PopDen":{
            "breaks":[3000,7000,20000,42000,76000],
            "name":"Population Density"
        },
        "Immi%":{
            "breaks":[30,45,55,65,76],
            "name": "Immigrant Percentage"
        },
        "VM%":{
            "breaks":[30,45,65,80,99],
            "name": "Visible Minority Percentage"
        },
        "LIn%":{
            "breaks":[7,15,20,25,40],
            "name":"Low Income Population Percentage"
        }
    }

    var color = scaleThreshold()
        .domain(demoGPs[demoGP]["breaks"])
        .range(ledColours);

    let divWidth = 400;
	$: innerWidth = divWidth;
	$: height = (innerWidth * 40) / 80;

	$: projection = geoMercator()
		.center([-78.17 - 0.0023*innerWidth + 0.000001125*innerWidth**2, 43.5 + 0.00045*innerWidth - 2.5e-7*innerWidth**2])
		.scale([76000 * innerWidth / 800])
		.angle([-17]);
	$: path = geoPath(projection);

    ctData.map((item =>{
        item.properties[demoGP]
        ?(item.properties["color_"+demoGP] = color(item.properties[demoGP]))
        :(item.properties["color_"+demoGP] = "white");
    }))

</script>

<div bind:offsetWidth={divWidth}>
	<svg width={innerWidth} {height} id={demoGP}>

        <text class="label" x="12" y="22">{demoGPs[demoGP].name}</text>
        
        {#each ctData as data}
            <path class="ct" d={path(data)} fill={data.properties["color_"+demoGP]}/>
        {/each}

        <text class="label" x="320" y="185">Demographic Group</text>
		<text class="label" x="320" y="200">(Value)</text>
		<text class="label" x="373" y="170">{demoGPs[demoGP]["breaks"][4]+ "%"}</text>
        <text class="label" x="373" y="170">{demoGPs[demoGP]["breaks"][3]+ "%"}</text>
		<text class="label" x="373" y="185">{demoGPs[demoGP]["breaks"][2]+ "%"}</text>
		<text class="label" x="373" y="200">{demoGPs[demoGP]["breaks"][1]+ "%"}</text>
		<text class="label" x="373" y="215">{demoGPs[demoGP]["breaks"][0]+ "%"}</text>

        <rect class="box" width="20" height = "15" x="350" y="150" style="fill:{ledColours[4]}; stroke: white;"></rect>
		<rect class="box" width="20" height = "15" x="350" y="165" style="fill:{ledColours[3]}; stroke: white;"></rect>
		<rect class="box" width="20" height = "15" x="350" y="180" style="fill:{ledColours[2]}; stroke: white;"></rect>
		<rect class="box" width="20" height = "15" x="350" y="195" style="fill:{ledColours[1]}; stroke: white;"></rect>
		<rect class="box" width="20" height = "15" x="350" y="210" style="fill:{ledColours[0]}; stroke: white;"></rect>


    </svg>
</div>


<style>
.mapGrid {
    margin: auto;
    padding-bottom: 42px;
    max-width: 850px;
    width: 100%;
    display: grid;
    gap: 4px 2px;
    grid-template-columns: repeat(2, 1fr);
}
.mapSmall {
    margin: auto;
    padding: -10px;
    max-width: 420px;
    width: 420px;
    margin: 0 auto;
}
.ct {
		stroke: rgb(237, 237, 237);
		stroke-width: 1px;
		opacity: 0.9;
}
.label {
		font-size: 13px;
		fill: rgb(56, 56, 56);
	}
</style>