

async function getLocation(startLong: number, startLat: number, destinationLong: number, destinationLat: number, distance: number): Promise<{ long: number, lat: number }> {
    const response = await fetch(`/location?start_long=${startLong}&start_lat=${startLat}&destination_long=${destinationLong}&destination_lat=${destinationLat}&distance=${distance}`, {
        method: 'GET',
    });
    if (!response.ok) {
        throw new Error('Network response was not ok');
    }
    return await response.json();
}


async function getFunFacts(long: number, lat: number): Promise<{ text: string }> {
    const response = await fetch(`/funfacts?long=${long}&lat=${lat}`, {
        method: 'GET',
    });
    if (!response.ok) {
        throw new Error('Network response was not ok');
    }
    return await response.json();
}


async function getAudioGuide(long: number, lat: number): Promise<Blob> {
    const response = await fetch(`/audioguide?long=${long}&lat=${lat}`, {
        method: 'GET',
    });
    if (!response.ok) {
        throw new Error('Network response was not ok');
    }
    return await response.blob();
}
