
<script lang='ts'>
    import LocationPicker from "./locationPicker.svelte"
</script>

<div id=routeplanner>
    <LocationPicker label="Pick a start location"/>
    <LocationPicker label="Pick a destination"/>

    <input type="range" min="1" max="10" value="1" id="mySlider">

</div>
