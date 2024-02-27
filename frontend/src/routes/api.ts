import {type location } from "./lcoation_search";

const backend_url = 'http://localhost:5000';
// const backend_url = 'http://10.52.249.109:5000';


export async function getLocation(start:location|string, end:location|string, distance: number): Promise<location> {
    const startparam = typeof start === 'string' ? `start=${start}` : `start_long=${start.lon}&start_lat=${start.lat}`;
    const endparam = typeof end === 'string' ? `destination=${end}` : `destination_long=${end.lon}&destination_lat=${end.lat}`;
    const response = await fetch(`${backend_url}/location?${startparam}&${endparam}&distance=${distance}`, {
        method: 'GET',
    });
    if (!response.ok) {
        throw new Error('Network response was not ok:' + response.status);
    }
    const json = await response.json();
    return { name: '?', lon: json.long, lat: json.lat };
}


export async function getFunFacts(loc:location): Promise<{ text: string }> {
    const response = await fetch(`${backend_url}/funfacts?long=${loc.lon}&lat=${loc.lat}`, {
        method: 'GET',
    });
    if (!response.ok) {
        throw new Error('Network response was not ok:' + response.status);
    }
    return await response.json();
}


export async function getAudioGuide(long:location): Promise<Blob> {
    const response = await fetch(`${backend_url}/audioguide?long=${long.lon}&lat=${long.lat}`, {
        method: 'GET',
    });
    if (!response.ok) {
        throw new Error('Network response was not ok:' + response.status);
    }
    return await response.blob();
}
