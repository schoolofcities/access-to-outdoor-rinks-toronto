<script>

	import { onMount } from 'svelte';
	import maplibregl, { LineBucket } from 'maplibre-gl';
	import "../assets/maplibre-gl.css";
	import "../assets/global-styles.css";
	import rinks from '../assets/toronto-rinks.geo.json';
	import municipalBoundaries from '../assets/toronto-former-municipal-boundaries.geo.json';
	import municipalPoints from '../assets/toronto-former-municipal-points.geo.json';
	import travelTime from "../assets/toronto-hex-grid-v2.geo.json";
	import notToronto from '../assets/toronto-not.geo.json';
	import subwayLines from '../assets/subway_lines.geo.json';
	import busRoutes from '../assets/busPath.geo.json';
	import mapStyle from '../assets/style.json';

	console.log(mapStyle);
	

	let pageHeight;
	let pageWidth;
	let map;

	let mapHeight = 600;
	$: if (pageHeight < 800) {
		mapHeight = pageHeight - 200;
	} else {
		mapHeight = 600
	}

	onMount(() => {

		map = new maplibregl.Map({
			container: 'map',
			style: mapStyle,
			center: [-79.36, 43.715], // starting position
			zoom: 10.5, // starting zoom;
			minZoom: 9,
			maxZoom: 13,
			bearing: -17,
			maxBounds:[ 
				[-80.28, 43.21], 
				[-77.88, 44.91] 
			],
			projection: 'globe',
			scrollZoom: true,
			attributionControl: false,
			showZoom: true,
		});

		let scale = new maplibregl.ScaleControl({
			maxWidth: 100,
			unit: 'metric',
		});

		let nav = new maplibregl.NavigationControl({
			showZoom: true, 
			showCompass: false,
		});

		map.addControl(scale, 'bottom-right');
		map.addControl(nav, 'top-right'); //add the zoom button panel to the map

		map.dragRotate.disable();
		map.touchZoomRotate.disableRotation();
		map.scrollZoom.disable();


		map.on('load', () => {

			map.addSource('TravelTime',{
				type: 'geojson',
				data: travelTime
			})

			map.addLayer({
				'id': 'walkTime',
				'type': 'fill',
				'source': 'TravelTime',
				'layout': {
					visibility: 'visible'
				},
				'paint': {
					'fill-color': [
						'step',
						['get', 'w'],
						"#FF0000",
						0, "#f1eef6",
						15, '#bdc9e1',
						30, '#74a9cf',
						45, '#2b8cbe',
						60, '#045a8d',
					],
					'fill-opacity': 1,
				}
			})

			//layer - travel time by transit - weekday
			map.addLayer({
				'id': 'transitWeekday',
				'type': 'fill',
				'source': 'TravelTime',
				'layout': {
					visibility: 'none'
				},
				'paint': {
					'fill-color': [
						'step',
						['get', 't'],
						"#FF0000",
						0, "#f1eef6",
						15, '#bdc9e1',
						30, '#74a9cf',
						45, '#2b8cbe',
						60, '#045a8d',
					],
					'fill-opacity': 1,
				}
			})

			//layer - travel time by transit - weekend
			map.addLayer({
				'id': 'transitWeekend',
				'type': 'fill',
				'source': 'TravelTime',
				'layout': {
					visibility: 'none'
				},
				'paint': {
					'fill-color': [
						'step',
						['get', 't'],
						"#FF0000",
						0, "#f1eef6",
						15, '#bdc9e1',
						30, '#74a9cf',
						45, '#2b8cbe',
						60, '#045a8d',
					],
					'fill-opacity': 1,
				}
			})
			

			map.addSource('notToronto', {
				type: 'geojson',
				data: notToronto
			})
			map.addLayer({
				'id': 'notToronto',
				'type': 'fill',
				'source': 'notToronto',
				'paint': {
					'fill-color': '#ffffff',
					'fill-opacity': 1,
				}
			})
			
			map.addSource('bus',{
				type: 'geojson',
				data : busRoutes
			})
			map.addLayer({
				'id': 'bus',
				'type': 'line',
				'source': 'bus',
				'layout':{
					visibility: "visible"
				},
				'paint': {
					'line-color': "#fff",
					'line-width': 1,
					'line-opacity': 0.2
				}
			})

			map.addSource('osm-raster-tiles', {
				'type': 'raster',
				'tiles': ['https://tile.openstreetmap.org/{z}/{x}/{y}.png'],
				'tileSize': 256,
				'minzoom': 0,
				'maxzoom': 19
			});
			map.addLayer({
				'id': 'osm-raster-tiles',
				'type': 'raster',
				'source': 'osm-raster-tiles',
				'paint': {
					'raster-saturation': -1,
					'raster-opacity': 0.14
				}
			})	

			

			map.addSource('subway',{
				type: 'geojson',
				data : subwayLines
			})
			map.addLayer({
				'id': 'subway',
				'type': 'line',
				'source': 'subway',
				'layout':{
					visibility: "visible"
				},
				'paint': {
					'line-color': "#666464",
					'line-width': 1
				}
			})

			map.addSource('municipalBoundaries', {
				type: 'geojson',
				data: municipalBoundaries
			})
			map.addLayer({
				'id': 'municipalBoundaries',
				'type': 'line',
				'source': 'municipalBoundaries',
				'paint': {
					'line-color': '#1E3765',
					'line-opacity': 0.3
				}
			})

			map.addLayer({
				'id': 'notTorontoStroke',
				'type': 'line',
				'source': 'notToronto',
				'paint': {
					'line-color': "#1E3765",
					'line-width': 1.5
				}
			})

			map.addSource('municipalPoints', {
				type: 'geojson',
				data: municipalPoints
			})
			map.addLayer({
				'id': 'municipalPoints',
				'type': 'symbol',
				'source': 'municipalPoints',
				'layout': {
					'text-field': ['get', 'AREA_NAME'],
					"text-font": ["TradeGothic LT Regular"],
					'text-size': 13
				},
					'paint': {
					'text-color': '#1E3765',
					'text-halo-color': 'white',
					'text-halo-width': 1,
					'text-halo-blur': 2
				}
			})


			map.addSource('rinks', {
				type: 'geojson',
				data: rinks
			})
			map.addLayer({
				'id': 'rinks',
				'type': 'circle',
				'source': 'rinks',
				'paint': {
					"circle-color": "#000",
					"circle-radius" : 4.2,
					"circle-stroke-color": "#fff",
					"circle-stroke-width": 2
				}
			})


			const toggleableLayerIds = {"walkTime": "Walk", "transitWeekday": "Public Transit"};

			for (const id in toggleableLayerIds) {

				if(!map.getLayer(id)) {
					continue;
				}
	
				//create a link
				const link = document.createElement("a");
				link.id = id;
				link.href = "#";
				link.textContent = toggleableLayerIds[id];
				if (id === "walkTime") {
					link.className = "active";
				}
				

				//show or hide layer when the toggle is clicked
				link.onclick = function (e) {
					const clickedLayer = this.id;
					e.preventDefault();
					e.stopPropagation();

					// Set clicked button to active and show map layer
					this.className = "active";
					map.setLayoutProperty(clickedLayer, 
						'visibility', 
						'visible'
					);
					
					// For others, set button not active and map layers not shown
					for(const other in toggleableLayerIds) {
						if (other === clickedLayer) {
							continue;
						}

						const button = document.getElementById(other);
						button.className = " "
						map.setLayoutProperty(other, 
							'visibility', 
							'none'
						);
					}
				};
				const layers = document.getElementById('menu');
				layers.appendChild(link);
			}


		})
	});


</script>

<svelte:window bind:innerHeight={pageHeight} bind:innerWidth={pageWidth}/>




<div id="menu"></div>

<div id="map" style="height: {mapHeight}px"></div>

<p>Data Sources: OpenStreetMap, City of Toronto, Toronto Transit Commission</p>

<style>
	#map {
		width: 100%;
		margin: 0 auto;
		max-width: 1200px;
		border-top: 1px solid var(--brandLightBlue);
		border-bottom: 1px solid var(--brandLightBlue);
		background-color: white;
	}
	p {
		margin: 0 auto;
		text-align: right;
		font-size: 10px;
		max-width: 1200px;
		color: var(--brandMedBlue);
	}
	#menu {
		margin: 0 auto;
		margin-top: -10px;
		max-width: 750px;
		background: #fff;
		position: relative;
		padding-top: -10px;
		padding-bottom: 10px;
		/* display: inline-block; */
		z-index: 1;
		border-radius: 0px;
		width: 100%;
		font-family: 'Open Sans', sans-serif;
		text-align: left;
		padding-left: 15px;
	}
	#menu :global(a) {
		font-size: 13px;
		color: var(--brandDarkBlue);
		display: inline-block;
		padding: 5px;
		padding-left: 8px;
		padding-right: 8px;
		margin-right: 10px;
		margin-bottom: 10px;
		width: 100px;
		border: 1px solid var(--brandDarkBlue);
		border-radius: 4px;
		text-decoration: none;
		text-align: center;
	}

	#menu :global(a):hover {
		background-color: var(--brandMedBlue);
		color: var(--brandWhite);
	}
	#menu :global(a.active) {
		background-color: var(--brandDarkBlue);
		color: var(--brandWhite);
	}
	#menu :global(a.active):hover {
		background: var(--brandDarkBlue);
	}

</style>
