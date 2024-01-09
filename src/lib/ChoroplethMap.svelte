<script>

    import { geoPath, geoMercator, scaleThreshold } from "d3"; 
    import ctData from "../assets/ctData.geo.json"; //the census data by CT
    import rinks from "../assets/toronto-rinks.geo.json";
    import border from "../assets/toronto-former-municipal-boundaries.geo.json"
    import municipalPoints from '../assets/toronto-former-municipal-points.geo.json';
    
    var ledColours = ["#ede9fe", "#dad9f9", "#aaacd4", "#6e6d9f", "#383669"] 
    // var ledColours = ["#975e86", "#bb8f90", "#dec09a", "#ffeea3"] // // // //

    export let demoGP;

    const barData = [
            {
                mode: "Walk",
                populationTime: 34.3,
                LIncomeTime: 33.5,
                ImmigrantTime: 37.0,
                VMTime: 39.7,
            },
            {
                mode: "Transit",
                populationTime: 23.4,
                LIncomeTime: 22.7,
                ImmigrantTime: 24.5,
                VMTime: 25.4,
            }
        ];
    
    const demoGPs = {
        "PopDen":{
            "breaks":[2500,5000,7500],
            "name":"Population Density (# of people per sq.km)",
            "breakSuffix": "",
            "barChartText": "overall population",
            "walkTime": 34.3,
            "transitTime": 23.4
        },
        "Immi%":{
            "breaks":[30,45,60],
            "name": "Immigrant (% of population)",
            "breakSuffix": "%",
            "barChartText": "immigrant population",
            "walkTime": 37,
            "transitTime": 24.5
        },
        "VM%":{
            "breaks":[30,45,60],
            "name": "Visible Minority (% of population)",
            "breakSuffix": "%",
            "barChartText": "visible minorities",
            "walkTime": 39.7,
            "transitTime": 25.4
        },
        "LIn%":{
            "breaks":[5,10,15],
            "name":"Low Income (% of population)",
            "breakSuffix": "%",
            "barChartText": "low-income residents",
            "walkTime": 33.5,
            "transitTime": 22.7
        }
    }

    var color = scaleThreshold()
        .domain(demoGPs[demoGP]["breaks"])
        .range(ledColours);

    let divWidth;
	$: innerWidth = divWidth;
	$: height = innerWidth / 1.55;

    $: console.log(divWidth);

    $: projection = geoMercator()
            .center([-79.188 + 0.24 * ((600 - innerWidth) / 200), 43.727 - 0.02 * ((600 - innerWidth) / 200) ])
            .scale([62000 * innerWidth / 600])
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

<div id="container" bind:offsetWidth={divWidth}>

	<svg width={innerWidth} {height} id={demoGP}>

        <text class="label" x="5" y="22">{demoGPs[demoGP].name}</text>
        
        {#each border.features as data}
            <path d={path(data)} stroke="#1E3765" stroke-width=6 fill=none opacity=0.23/>
        {/each}

        {#each ct as data}
            <path class="ct" d={path(data)} fill={data.properties["color_"+demoGP]}/>
        {/each}

        {#each border.features as data}
            <path d={path(data)} stroke="#1E3765" stroke-width=1 fill=none opacity=0.8/>
        {/each}

        {#each toRinks as data}
            <circle
            class="rink"
            cx={projection(data.geometry.coordinates)[0]}
            cy={projection(data.geometry.coordinates)[1]}
            r="4"
            stroke="white"
            stroke-width="2"
            fill="black"/>
        {/each}

        {#each municipalPoints.features as data}
			<text
				class="legend"
				x={projection(data.geometry.coordinates)[0]}
				y={projection(data.geometry.coordinates)[1]}
				text-anchor="middle"
				stroke="white"
				stroke-width=2
				font-size=12
				opacity=0.7
				>{data.properties.AREA_NAME}
			</text>
			<text
				class="legend"
				x={projection(data.geometry.coordinates)[0]}
				y={projection(data.geometry.coordinates)[1]}
				text-anchor="middle"
				font-size=12
				>{data.properties.AREA_NAME}
			</text>
		{/each}

        <rect class="box" width="70" height = "12" x="215" y="30" style="fill:{ledColours[3]}; stroke: white;"></rect>
        <rect class="box" width="70" height = "12" x="145" y="30" style="fill:{ledColours[2]}; stroke: white;"></rect>
		<rect class="box" width="70" height = "12" x="75" y="30" style="fill:{ledColours[1]}; stroke: white;"></rect>
		<rect class="box" width="70" height = "12" x="5" y="30" style="fill:{ledColours[0]}; stroke: white;"></rect>

        <text class="label legend" x="215" y="55" text-anchor="middle">{demoGPs[demoGP]["breaks"][2]+ demoGPs[demoGP].breakSuffix}</text>
		<text class="label legend" x="145" y="55" text-anchor="middle">{demoGPs[demoGP]["breaks"][1]+ demoGPs[demoGP].breakSuffix}</text>
		<text class="label legend" x="75" y="55" text-anchor="middle">{demoGPs[demoGP]["breaks"][0]+ demoGPs[demoGP].breakSuffix}</text>
        


    </svg>

    <svg width={innerWidth} height="60">

        <text class="label legend" x="50" y="{10}" text-anchor="start">Average travel time to nearest rink ({demoGPs[demoGP]["barChartText"]})</text>

        <text class="label legend" x="46" y="{28}" text-anchor="end">Walk</text>
        <rect class="bar" width="{250 * demoGPs[demoGP]["walkTime"] / 40}" height = "8" x="50" y="{20}" style="fill: #6D247A; stroke: white;"></rect>
        <text class="label legend" x="{53 + 250 * demoGPs[demoGP]["walkTime"] / 40}" y="{28}" text-anchor="start">{demoGPs[demoGP]["walkTime"]} minutes</text>

        <text class="label legend" x="46" y="{48}" text-anchor="end">Transit</text>
        <rect class="bar" width="{250 * demoGPs[demoGP]["transitTime"] / 40}" height = "8" x="50" y="{40}" style="fill: #6D247A; stroke: white;"></rect>
        <text class="label legend" x="{53 + 250 * demoGPs[demoGP]["transitTime"] / 40}" y="{48}" text-anchor="start">{demoGPs[demoGP]["transitTime"]} minutes</text>
        
    </svg>

</div>


<style>
    #container {
        width: 100%;
        max-width: 600px;
        min-width: 400px;
    }
    .rink{
        stroke: var(--brandWhite);
        stroke-width: 1px;
        fill: var(--brandGray90)
    }
    .ct {
        stroke: var(--brandWhite);
        stroke-width: 0.5px;
        opacity: 0.75;
    }
    .box {
        opacity: 0.75;
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