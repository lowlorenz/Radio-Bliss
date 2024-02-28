
<script lang='ts'>
    import { getAudioGuide, getFunFacts, getLocation } from "./api";
    import type { location } from "./lcoation_search";
    import LocationPicker from "./locationPicker.svelte"
    import MapView from "./mapView.svelte";
    import { browser } from '$app/environment';

    const synth = browser ? window.speechSynthesis : null;

    var startLocation :location | string = 'Berlin'
    var destLocation :location | string = 'Hamburg'
    var text: string = 'loading...'

    var progress:number = 0.5

    let displaylocation = {lat:52, lon:13}

    function startRoute(){
        text = "loading..."
        if (synth) synth.cancel();  // stop speaking when a new request is send
        getLocation(startLocation!, destLocation!, progress)
            .then(loc=>{
                displaylocation = loc
                return loc;
            })
            .catch(err=>{
                console.log(err)
                if (typeof startLocation !== 'string' && typeof destLocation !== 'string') {
                    displaylocation = {lat: startLocation!.lat * (1-progress) + destLocation!.lat * (progress), lon: startLocation!.lon * (1-progress) + destLocation!.lon * (progress)}
                }
                return displaylocation;
            })
            .then(loc=>{
                if (document.cookie.includes('nice')) {
                    getAudioGuide(loc).then(playAudio)
                }
                return getFunFacts(loc);
            })
            .then(facts=>{
                text = facts.text;
                if (synth && !document.cookie.includes('nice')) {
                    synth.cancel();
                    const utterThis = new SpeechSynthesisUtterance(facts.text);
                    synth.speak(utterThis);
                }
            })
    }


    function playAudio(mp3Blob: Blob) {
        // Create a Blob URL from the Blob
        var blobUrl = URL.createObjectURL(mp3Blob);

        // Create a new Audio element
        var audio = new Audio();

        // Set the source of the audio element to the Blob URL
        audio.src = blobUrl;

        // Play the audio
        audio.play()
            .then(() => console.log("Playback started"))
            .catch(error => console.error("Error playing the audio", error));

        // Revoke the Blob URL to free up resources
        // This can be done after the audio is no longer needed
        audio.onended = () => {
            URL.revokeObjectURL(blobUrl);
            console.log("Blob URL revoked");
        };
    }


</script>

<div id=parentcontainer>

    <MapView loc={displaylocation} start={startLocation} end={destLocation}/>

    <div id=routeplanner>
        <LocationPicker label="Pick a start location" onlocationchange={loc=>startLocation=loc} value="Berlin"/>
        <LocationPicker label="Pick a destination" onlocationchange={loc=>destLocation=loc} value="Hamburg"/>


        <input type="range" id = rangeslider min="0" max="1" step="0.1" bind:value={progress}>
        <p></p>

        <button id=routestart on:click={startRoute}>start</button>

        <p>start: {startLocation}</p>
        <p>destination: {destLocation}</p>
        <p>output location: {displaylocation.lon} {displaylocation.lat}</p>

        <p style="max-width:50vw">{text}</p>
    </div>

</div>