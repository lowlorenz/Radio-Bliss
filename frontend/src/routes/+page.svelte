
<script lang="ts">
    import LocationPicker from "./locationPicker.svelte"
    import MapView from "./mapView.svelte"

</script>


<h1>Welcome to Radio-Bliss</h1>


<div id=parentcontainer>
    <MapView/>
    <div id=routeplanner>
        <LocationPicker label="Pick a start location"/>
        <LocationPicker label="Pick a destination"/>
    </div>
</div>

