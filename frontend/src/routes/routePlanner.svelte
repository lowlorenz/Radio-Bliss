
<script lang='ts'>
    import { getFunFacts, getLocation } from "./api";
    import type { location } from "./lcoation_search";
    import LocationPicker from "./locationPicker.svelte"
    import MapView from "./mapView.svelte";

    var startLocation :location | null = null
    var destLocation :location | null = null
    var text: string = 'loading...'

    var progress:number = 5

    $: console.log(progress)

    let displaylocation = {name:"Berlin", lat:52, lon:13}

    function startRoute(){
        getLocation(startLocation!, destLocation!, progress)
            .then(loc=>{
                displaylocation = loc
                return loc;
            })
            .catch(err=>{
                console.log(err)
                displaylocation = {name:"path", lat: startLocation!.lat * (1-progress) + destLocation!.lat * (progress), lon: startLocation!.lon * (1-progress) + destLocation!.lon * (progress/10)}
                return displaylocation;
            })
            .then(loc=>getFunFacts(loc))
            .then(facts=>{
                text = facts.text;
            })
    }


</script>

<MapView loc={displaylocation}/>

<div id=routeplanner>
    <LocationPicker label="Pick a start location" onlocationchange={loc=>startLocation=loc} placeholder={"Berlin"}/>
    <LocationPicker label="Pick a destination" onlocationchange={loc=>destLocation=loc} placeholder={"Hamburg"}/>


    <input type="range" id = rangeslider min="0" max="1" step="0.1" bind:value={progress}>
    <p></p>

    <button id=routestart on:click={startRoute}>start</button>

    <p>start: {startLocation?.lon} {startLocation?.lat}</p>
    <p>destination: {destLocation?.lon} {destLocation?.lat}</p>
    <p>output location: {displaylocation.lon} {displaylocation.lat}</p>

    <p>{text}</p>
</div>



