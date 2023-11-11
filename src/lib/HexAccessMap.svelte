<script>

	import { onMount } from 'svelte';
	import maplibregl, { LineBucket } from 'maplibre-gl';
	import "../assets/maplibre-gl.css";
	import rinks from '../assets/toronto-rinks.geo.json';
	import municipalBoundaries from '../assets/toronto-former-municipal-boundaries.geo.json';
	import hexGrid from '../assets/toronto-hex-grid.geo.json';
	import travelTime from "../assets/walk_time.geo.json";
	import notToronto from '../assets/toronto-not.geo.json';
	import subwayLines from '../assets/subway_lines.geo.json';
	import busRoutes from '../assets/bus_routes.geo.json';

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
			// style: './vector-tiles-vintage-v4.json',//'https://basemaps.cartocdn.com/gl/positron-gl-style/style.json',
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

		map.addSource('TravelTime',{
			type: 'geojson',
			data: travelTime
		})

		//layer - travel time by walking
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
					['get', 'walk_real'],
					"#FF0000",
					0, "#f1eef6",
					15, '#bdc9e1',
					30, '#74a9cf',
					45, '#2b8cbe',
					60, '#045a8d',
				],
				'fill-opacity': 0.75,
				// 'fill-outline-color': 'white',
			}
		})

		//layer - travel time by transit - weekday
		map.addLayer({
			'id': 'transitWeekday',
			'type': 'fill',
			'source': 'TravelTime',
			'layout': {
				visibility: 'visible'
			},
			'paint': {
				'fill-color': [
					'step',
					['get', 'transit_wd_real'],
					"#FF0000",
					0, "#f1eef6",
					15, '#bdc9e1',
					30, '#74a9cf',
					45, '#2b8cbe',
					60, '#045a8d',
				],
				'fill-opacity': 0.75,
				// 'fill-outline-color': 'white',
			}
		})

		//layer - travel time by transit - weekend
		map.addLayer({
			'id': 'transitWeekend',
			'type': 'fill',
			'source': 'TravelTime',
			'layout': {
				visibility: 'visible'
			},
			'paint': {
				'fill-color': [
					'step',
					['get', 'transit_we_real'],
					"#FF0000",
					0, "#f1eef6",
					15, '#bdc9e1',
					30, '#74a9cf',
					45, '#2b8cbe',
					60, '#045a8d',
				],
				'fill-opacity': 0.75,
				// 'fill-outline-color': 'white',
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
				'line-color': "#4d4d4d",
				'line-width': 2
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
				'line-color': "#D0D1C9",
				'line-width': 0.1
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
				'fill-opacity': 1
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
				'raster-opacity': 0.13
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
				'line-color': '#7d979e'
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
				"circle-color": "#6D247A",
				"circle-radius" : 3.5
			}
		})

		map.on('load', () => {
			const toggleableLayerIds = {"walkTime": "Walk", "transitWeekday": "Transit (Weekday)", "transitWeekend": "Transit (Weekend)"};

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

<div> 
	<nav id="menu"></nav> 
</div>

<p>
	15, 30, 45, 60
</p>

<div id="map" style="height: {mapHeight}px"></div>

<p>Data Sources: OpenStreetMap, City of Toronto</p>

<style>
	#map {
		width: 100%;
		margin: 0 auto;
		max-width: 1200px;
		border-top: 1px solid var(--brandMedBlue);
		border-bottom: 1px solid var(--brandMedBlue);
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
		background: #fff;
		position: relative;
		margin: 0 auto;
		display: inline;
		z-index: 1;
		top: 10px;
		right: 10px;
		border-radius: 0px;
		width: 120px;
		font-family: 'Open Sans', sans-serif;
	}
	#menu :global(a) {
		font-size: 13px;
		color: var(--brandDarkBlue);
		display: inline-block;
		padding: 10px 12px;
		margin-right: 10px;
		width: 120px;
		border: 1px solid var(--brandDarkBlue);
		border-radius: 4px;
		text-decoration: none;
		text-align: center;
	}

	#menu :global(a):hover {
	background-color: var(--brandDarkBlue);
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
