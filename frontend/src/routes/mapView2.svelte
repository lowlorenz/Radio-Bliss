<script lang="ts">
    import { onMount } from 'svelte';
    let mapElement;


    export var loc:location
    export var start:location|null
    export var end:location|null
    
  
    // Async function to load the Google Maps script
    async function loadGoogleMapsApi() {
      return new Promise((resolve) => {
        const script = document.createElement('script');
        script.src = `https://maps.googleapis.com/maps/api/js?key=AIzaSyCLTR5jt4ev0PdxstLdqYjuFUxeGnzVq7M`;
        script.async = true;
        script.defer = true;
        document.head.appendChild(script);
        script.onload = () => resolve(42);
      });
    }
  
    // Initialization function for the map and markers
    async function initMap(loc, start, end) {
      await loadGoogleMapsApi(); // Ensure the API is loaded
  
      const map = new google.maps.Map(mapElement, {
        zoom: 6,
        center: { lat: loc.lat, lng: loc.lon }, // Default center
      });
  
      const directionsService = new google.maps.DirectionsService();
      const directionsRenderer = new google.maps.DirectionsRenderer({
        map: map,
        suppressMarkers: true, // Do not show default markers
      });
  
      if (!start || !end) return;
      console.log(start, end);
      const startLocation = new google.maps.LatLng(start.lat, start.lon); // Start location
      const endLocation = new google.maps.LatLng(end.lat, start.lon); // End location
  
      // Repeat your marker setup here...
  
      const request = {
        origin: startLocation,
        destination: endLocation,
        travelMode: 'DRIVING',
      };
  
      directionsService.route(request, function (response, status) {
        if (status === 'OK') {
          directionsRenderer.setDirections(response);
          // Your marker logic...
        } else {
          window.alert('Directions request failed due to ' + status);
        }
      });
    }
  
    // Use onMount to ensure this runs when the component is mounted
    onMount(() => {
      initMap(loc, start, end);
    });
  </script>
  
  <style>
    #map {
      height: 400px;
      width: 300px;
    }
  </style>
  
  <div bind:this={mapElement} id="map"></div>
  