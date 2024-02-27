
<script lang='ts'>
    import { getLocation } from "./api";
    import type { location } from "./lcoation_search";
    import LocationPicker from "./locationPicker.svelte"

    var startLocation :location | null = null
    var destLocation :location | null = null

    var progress:number = 5

    $: console.log(progress)

    function startRoute(){
        let location = getLocation(startLocation!, destLocation!, progress/10)
    }

</script>

<div id=routeplanner>
    <LocationPicker label="Pick a start location" onlocationchange={loc=>startLocation=loc} placeholder={"Berlin"}/>
    <LocationPicker label="Pick a destination" onlocationchange={loc=>destLocation=loc} placeholder={"Hamburg"}/>


    <input type="range" id = rangeslider min="1" max="10" bind:value={progress}>
    <p></p>

    <button id=routestart on:click={startRoute}>start</button>

</div>



