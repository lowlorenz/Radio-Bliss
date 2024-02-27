
import {type location } from "./lcoation_search";

export async function getLocation(start:location, end:location, distance: number): Promise<{ long: number, lat: number }> {
    const response = await fetch(`/location?start_long=${start.lon}&start_lat=${start.lat}&destination_long=${end.lon}&destination_lat=${end.lat}&distance=${distance}`, {
        method: 'GET',
    });
    if (!response.ok) {
        throw new Error('Network response was not ok');
    }
    return await response.json();
}


export async function getFunFacts(loc:location): Promise<{ text: string }> {
    const response = await fetch(`/funfacts?long=${loc.lon}&lat=${loc.lat}`, {
        method: 'GET',
    });
    if (!response.ok) {
        throw new Error('Network response was not ok');
    }
    return await response.json();
}


export async function getAudioGuide(long:location): Promise<Blob> {
    const response = await fetch(`/audioguide?long=${long.lon}&lat=${long.lat}`, {
        method: 'GET',
    });
    if (!response.ok) {
        throw new Error('Network response was not ok');
    }
    return await response.blob();
}
