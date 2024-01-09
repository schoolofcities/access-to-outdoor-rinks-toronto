<script>

	import { geoPath, geoMercator, scaleThreshold } from "d3"; 
	import rinks from "../assets/toronto-rinks.geo.json";
	import border from "../assets/toronto-former-municipal-boundaries.geo.json";
	import notToronto from '../assets/toronto-not.geo.json';
	import hexVoronoi from "../assets/hex-grid-voronoi.geo.json";
	
	var ledColours = ["#ede9fe", "#dad9f9", "#aaacd4", "#6e6d9f", "#383669"];
	// var ledColours = ["#975e86", "#bb8f90", "#dec09a", "#ffeea3"] // // // //

	let divWidth;
	$: innerWidth = divWidth;
	$: height = innerWidth / 1.6;

	$: console.log(divWidth);

	$: projection = geoMercator()
			//.center([-78.155 - 0.00239*innerWidth + 0.000001125*innerWidth**2, 43.545 + 0.00045*innerWidth - 1.8e-7*innerWidth**2])
			.center([-79.2 + 0.21 * ((600 - innerWidth) / 200), 43.727 - 0.02 * ((600 - innerWidth) / 200) ])
			.scale([62000 * innerWidth / 600])
			.angle([-17]);
	$: path = geoPath(projection);

	let toRinks = rinks.features;



</script>

<div id="container" bind:offsetWidth={divWidth}>

	<svg width={innerWidth} {height}>

		
		{#each border.features as data}
			<path d={path(data)} stroke="#6FC7EA" stroke-width=6 fill=none opacity=0.23/>
		{/each}

		{#each hexVoronoi.features as data}
			{#if data.properties.c === "l"}
				<path d={path(data)} stroke="#fff" stroke-width=0.5 fill="#f0d5e4" opacity=0.8/>
			{:else if data.properties.c === "m"}
				<path d={path(data)} stroke="#fff" stroke-width=0.5 fill="#dd9ec1" opacity=0.8/>
			{:else if data.properties.c === "h"}
				<path d={path(data)} stroke="#fff" stroke-width=0.5 fill="#ab1368" opacity=0.8/>
			{:else}
				<path d={path(data)} stroke="#fff" stroke-width=0.5 fill="#888888" opacity=0.8/>
			{/if}
		{/each}

		{#each notToronto.features as data}
			<path d={path(data)} stroke="#6FC7EA" stroke-width=0 fill="white" opacity=0.99/>
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

		<text class="label" x="5" y="22">Total population in each outdoor rink's catchment area</text>
		
		

        <rect class="box" width="70" height = "16" x="145" y="35" style="fill:#ab1368; stroke: white;"></rect>
		<rect class="box" width="70" height = "16" x="75" y="35" style="fill:#dd9ec1; stroke: white;"></rect>
		<rect class="box" width="70" height = "16" x="5" y="35" style="fill:#f0d5e4; stroke: white;"></rect>
		
		<text class="legend" x="25" y="48">{"< 50k"}</text>
		<text class="legend" x="82" y="48">{"50k - 100k"}</text>
		<text class="legend-dark" x="160" y="48">{"100k +"}</text>

		<rect class="box" width="16" height = "16" x="225" y="35" style="fill:#888888; stroke: white;"></rect>
		<text class="legend" x="243" y="48">60+ min to nearest rink</text>

	</svg>

</div>


<style>
	#container {
		margin: 0 auto;
		width: 100%;
		max-width: 600px;
		min-width: 400px;
		border-top: solid 1px var(--brandLightBlue);
		border-bottom: solid 1px var(--brandLightBlue);

	}
	.rink{
		stroke: var(--brandWhite);
		stroke-width: 1px;
		fill: var(--brandGray90)
	}
	.label {
			font-size: 14px;
			font-weight: 600;
			fill: var(--brandDarkBlue);
		}
	.legend {
		font-size: 13px;
		font-weight: 400;
		fill: var(--brandDarkBlue);
	}
	.legend-dark {
		font-size: 13px;
		font-weight: 400;
		fill: var(--brandWhite);
	}
</style>