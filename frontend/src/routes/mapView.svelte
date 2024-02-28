<script lang="ts">
    import { onMount } from "svelte";
    import type { location } from "./lcoation_search";


	export var loc:location
	export var start:location|string
	export var end:location|string

	let container : HTMLDivElement
	
	let update= (loc:location)=>{
		if (false && start && end) {
			if (typeof start !== 'string')
				start = `${start.lat},${start.lon}`
			if (typeof end !== 'string')
				end = `${end.lat},${end.lon}`
			const loc_str = `${loc.lat},${loc.lon}`
			container.innerHTML = `<iframe width="300" height="550" frameborder="0"  src="https://maps.google.com/maps?f=d&saddr=${start}&mrad=${loc.lat},${loc.lon}&daddr=${end}&dirflg=d&amp;output=embed"/>`
		} else {
			container.innerHTML = `<iframe frameborder="0"  src="https://maps.google.com/maps?q=${loc.lat},${loc.lon}&z=12&amp;output=embed"/>`
		}
	}
	onMount(()=>update(loc))

	$: if (container!=undefined) update(loc)

</script>

<div id="mapview" bind:this={container}>

</div>
