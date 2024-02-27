

export type location = {name:string, lat:number, lon:number}

export const template_locations=[
    {name : "Berlin" , lat : 52.5200, lon : 13.4050},
    {name : "Hamburg" , lat : 53.5511, lon : 9.9937},
    {name : "Munich" , lat : 48.1351, lon : 11.5820},
    {name : "Cologne" , lat : 50.9375, lon : 6.9603},
    {name : "Frankfurt" , lat : 50.1109, lon : 8.6821},
    {name : "Stuttgart" , lat : 48.7758, lon : 9.1829},
    {name : "Düsseldorf" , lat : 51.2277, lon : 6.7735},
    {name : "Dortmund" , lat : 51.5139, lon : 7.4653},
    {name : "Essen" , lat : 51.4556, lon : 7.0116},
    {name : "Leipzig" , lat : 51.3397, lon : 12.3731},
    {name : "Bremen" , lat : 53.0793, lon : 8.8017},
    {name : "Dresden" , lat : 51.0504, lon : 13.7373},
    {name : "Hanover" , lat : 52.3759, lon : 9.7320},
    {name : "Nuremberg" , lat : 49.4474, lon : 11.0767},
    {name : "Duisburg" , lat : 51.4344, lon : 6.7623},
]


export function location_completion(req: string): location[]{
    return template_locations.filter((location)=>{
        return location.name.toLowerCase().includes(req.toLowerCase())
    })
}