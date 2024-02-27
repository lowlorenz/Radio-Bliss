


<script lang="ts">
    import { onMount } from "svelte";
    import type { location } from "./lcoation_search";


	export var loc:location

	let container : HTMLDivElement
	
	let update= (loc:location)=>{
		container.innerHTML = `<iframe width="300" height="550" frameborder="0"  src="https://maps.google.com/maps?q=${loc.lat},${loc.lon}&z=14&amp;output=embed"/>`
	}
	onMount(()=>update(loc))

	$: if (container!=undefined) update(loc)

</script>

<div id="mapview" bind:this={container}>

</div>
