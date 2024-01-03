<script>

    import { geoPath, geoMercator, scaleThreshold } from "d3"; 
    import ctData from "../assets/ctData.geo.json"; //the census data by CT
    import rinks from "../assets/toronto-rinks.geo.json";
    import border from "../assets/toronto-former-municipal-boundaries.geo.json"
    
    var ledColours = ["#ede9fe", "#dad9f9", "#aaacd4", "#6e6d9f", "#383669"] 
    // var ledColours = ["#975e86", "#bb8f90", "#dec09a", "#ffeea3"] // // // //

    export let demoGP;
    
    const demoGPs = {
        "PopDen":{
            "breaks":[2500,5000,7500],
            "name":"Population Density (# of people per sq.km)",
            "breakSuffix": ""
        },
        "Immi%":{
            "breaks":[30,45,60],
            "name": "Immigrant (% of population)",
            "breakSuffix": "%"
        },
        "VM%":{
            "breaks":[30,45,60],
            "name": "Visible Minority (% of population)",
            "breakSuffix": "%"
        },
        "LIn%":{
        "breaks":[5,10,15],
            "name":"Low Income (% of population)",
            "breakSuffix": "%"
        }
    }

    var color = scaleThreshold()
        .domain(demoGPs[demoGP]["breaks"])
        .range(ledColours);

    let divWidth;
	$: innerWidth = divWidth;
	$: height = innerWidth / 1.5;

    $: console.log(divWidth);

    $: projection = geoMercator()
            //.center([-78.155 - 0.00239*innerWidth + 0.000001125*innerWidth**2, 43.545 + 0.00045*innerWidth - 1.8e-7*innerWidth**2])
            .center([-79.2 + 0.21 * ((600 - innerWidth) / 200), 43.727 - 0.02 * ((600 - innerWidth) / 200) ])
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
            <path d={path(data)} stroke="#6FC7EA" stroke-width=6 fill=none opacity=0.23/>
        {/each}

        {#each ct as data}
            <path class="ct" d={path(data)} fill={data.properties["color_"+demoGP]}/>
        {/each}

        {#each border.features as data}
            <path d={path(data)} stroke="#6FC7EA" stroke-width=1 fill=none opacity=0.8/>
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

        <rect class="box" width="70" height = "12" x="215" y="30" style="fill:{ledColours[3]}; stroke: white;"></rect>
        <rect class="box" width="70" height = "12" x="145" y="30" style="fill:{ledColours[2]}; stroke: white;"></rect>
		<rect class="box" width="70" height = "12" x="75" y="30" style="fill:{ledColours[1]}; stroke: white;"></rect>
		<rect class="box" width="70" height = "12" x="5" y="30" style="fill:{ledColours[0]}; stroke: white;"></rect>

        <text class="label legend" x="215" y="55" text-anchor="middle">{demoGPs[demoGP]["breaks"][2]+ demoGPs[demoGP].breakSuffix}</text>
		<text class="label legend" x="145" y="55" text-anchor="middle">{demoGPs[demoGP]["breaks"][1]+ demoGPs[demoGP].breakSuffix}</text>
		<text class="label legend" x="75" y="55" text-anchor="middle">{demoGPs[demoGP]["breaks"][0]+ demoGPs[demoGP].breakSuffix}</text>
        
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
            opacity: 1;
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