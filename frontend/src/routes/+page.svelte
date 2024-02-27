
<script lang="ts">
    import LocationPicker from "./locationPicker.svelte"
    import MapView from "./mapView.svelte"
    import RoutePlanner from "./routePlanner.svelte";


</script>


<h1>Welcome to Radio-Bliss</h1>


<div id=parentcontainer>

    <RoutePlanner />

    <div id=steeringwheel>
        <img src="steering_wheel.png" alt="steeringwheel" width="650" height="500">
    </div>
</div>

