<script>

	import { onMount } from 'svelte';
	import maplibregl from 'maplibre-gl';
	import "../assets/maplibre-gl.css";
	import rinks from '../assets/toronto-rinks.geo.json';
	import municipalBoundaries from '../assets/toronto-former-municipal-boundaries.geo.json';
	import hexGrid from '../assets/toronto-hex-grid.geo.json';
	import walkTime from "../assets/walk_time.geo.json";
	import notToronto from '../assets/toronto-not.geo.json';

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
			showCompass: true,
		});

		map.addControl(scale, 'bottom-right');
		map.addControl(nav, 'top-right'); //add the zoom button panel to the map

		map.dragRotate.disable();
		map.touchZoomRotate.disableRotation();
		map.scrollZoom.disable();

		map.addSource('walkTime',{
			type: 'geojson',
			data: walkTime
		})
		map.addLayer({
			'id': 'walkTime',
			'type': 'fill',
			'source': 'walkTime',
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
				'line-color': '#007FA3'
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
			})

	});

</script>




<svelte:window bind:innerHeight={pageHeight} bind:innerWidth={pageWidth}/>

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
</style>