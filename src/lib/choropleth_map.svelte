<script>
    import { onMount } from 'svelte';
    import * as d3 from 'd3';
    import { geoPath, geoMercator, scaleThreshold } from "d3"; 
    import ctData from "../assets/ctData.geo.json"; //the census data by CT
    import rinks from "../assets/toronto-rinks.geo.json";
    
    var ledColours = ["#ede9fe", "#dad9f9", "#aaacd4", "#6e6d9f", "#383669"] //colours for the map

    export let demoGP;
    
    const demoGPs = {
        "PopDen":{
            "breaks":[1000,3000,6000,12000,],
            "name":"Population Density (# of people in a sq.km)",
            "breakSuffix": ""
        },
        "Immi%":{
            "breaks":[30,45,55,65,],
            "name": "Immigrant Percentage",
            "breakSuffix": "%"
        },
        "VM%":{
            "breaks":[30,45,65,80,],
            "name": "Visible Minority Percentage",
            "breakSuffix": "%"
        },
        "LIn%":{
        "breaks":[7,15,20,25,],
            "name":"Low Income Population Percentage",
            "breakSuffix": "%"
        }
    }

    var color = scaleThreshold()
        .domain(demoGPs[demoGP]["breaks"])
        .range(ledColours);

    let divWidth = 600;
	$: innerWidth = divWidth;
	$: height = innerWidth / 1.75;

    $: projection = geoMercator()
            .center([-78.155 - 0.00239*innerWidth + 0.000001125*innerWidth**2, 43.54 + 0.00045*innerWidth - 2.5e-7*innerWidth**2])
            .scale([82000 * innerWidth / 800])
            .angle([-17]);
	$: path = geoPath(projection);

    let toRinks = rinks.features;
    let ct = ctData.features;

    ct.map((item =>{
        item.properties[demoGP]
        ?(item.properties["color_"+demoGP] = color(item.properties[demoGP]))
        :(item.properties["color_"+demoGP] = "white");
    }))


</script>

<div bind:offsetWidth={divWidth}>
	<svg width={innerWidth} {height} id={demoGP}>

        <text class="label" x="12" y="22">{demoGPs[demoGP].name}</text>
        
        {#each ct as data}
            <path class="ct" d={path(data)} fill={data.properties["color_"+demoGP]}/>
        {/each}

        {#each toRinks as data}
            <circle
            class="rink"
            cx={projection(data.geometry.coordinates)[0]}
            cy={projection(data.geometry.coordinates)[1]}
            r="2.5px"
            fill="black"/>
        {/each}

        <text class="label legend" x="475" y="268">{demoGPs[demoGP]["breaks"][3]+ demoGPs[demoGP].breakSuffix}</text>
		<text class="label legend" x="475" y="283">{demoGPs[demoGP]["breaks"][2]+ demoGPs[demoGP].breakSuffix}</text>
		<text class="label legend" x="475" y="298">{demoGPs[demoGP]["breaks"][1]+ demoGPs[demoGP].breakSuffix}</text>
		<text class="label legend" x="475" y="313">{demoGPs[demoGP]["breaks"][0]+ demoGPs[demoGP].breakSuffix}</text>

        <rect class="box" width="20" height = "15" x="450" y="250" style="fill:{ledColours[4]}; stroke: white;"></rect>
		<rect class="box" width="20" height = "15" x="450" y="265" style="fill:{ledColours[3]}; stroke: white;"></rect>
		<rect class="box" width="20" height = "15" x="450" y="280" style="fill:{ledColours[2]}; stroke: white;"></rect>
		<rect class="box" width="20" height = "15" x="450" y="295" style="fill:{ledColours[1]}; stroke: white;"></rect>
		<rect class="box" width="20" height = "15" x="450" y="310" style="fill:{ledColours[0]}; stroke: white;"></rect>


    </svg>
</div>


<style>
.rink{
    stroke: var(--brandWhite);
    stroke-width: 1px;
    fill: var(--brandGray90)
}
.ct {
		stroke: var(--brandGray);
		stroke-width: 1px;
		opacity: 0.9;
}
.label {
		font-size: 14px;
        font-weight: 600;
		fill: var(--brandDarkBlue);
	}
.legend {
    font-size: 13px;
    font-weight: 400;
}
</style>