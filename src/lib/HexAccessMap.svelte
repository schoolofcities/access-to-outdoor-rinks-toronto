<script>

	import { onMount } from 'svelte';
	import maplibregl from 'maplibre-gl';
	import "../assets/maplibre-gl.css";

	let pageHeight;
	let pageWidth;

	let mapHeight = 600;
	$: if (pageHeight < 800) {
		mapHeight = pageHeight - 200;
	} else {
		mapHeight = 600
	}

	onMount(() => {

		const maxBounds = 

		map = new maplibregl.Map({
			container: 'map',
			// style: './vector-tiles-vintage-v4.json',//'https://basemaps.cartocdn.com/gl/positron-gl-style/style.json',
			center: [-79.38, 43.71], // starting position
			zoom: 10.5, // starting zoom;
			minZoom: 9,
			maxZoom: 14,
			bearing: -17,
			maxBounds:[ 
				[-80.28, 43.21], 
				[-77.88, 44.91] 
			],
			projection: 'globe',
			scrollZoom: true,
			attributionControl: false,
		});

		let scale = new maplibregl.ScaleControl({
			maxWidth: 100,
			unit: 'metric',
		});
		map.addControl(scale, 'bottom-right');

		map.addSource('raster-tiles', {
			'type': 'raster',
			'tiles': ['https://tile.openstreetmap.org/{z}/{x}/{y}.png'],
			'tileSize': 256,
			'minzoom': 0,
			'maxzoom': 19
        });

		map.addLayer({
			'id': 'simple-tiles',
			'type': 'raster',
			'source': 'raster-tiles',
			'paint': {
				'raster-saturation': -1,
				'raster-opacity': 0.15
			}
		})


	
	});

</script>




<svelte:window bind:innerHeight={pageHeight} bind:innerWidth={pageWidth}/>





<div id="map" style="height: {mapHeight}px">

</div>




<style>
	#map {
		width: 100%;
		margin: 0 auto;
		max-width: 1200px;
		border-top: 1px solid var(--brandMedBlue);
		border-bottom: 1px solid var(--brandMedBlue);
		background-color: white;
	}
</style>