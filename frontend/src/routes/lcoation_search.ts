
export const template_locations=[
    "Berlin",
    "Hamburg",
    "Munich",
    "Cologne",
    "Frankfurt",
    "Stuttgart",
    "Düsseldorf",
    "Dortmund",
    "Essen",
]


export function location_completion(req: string){
    return template_locations.filter((location)=>{
        return location.toLowerCase().includes(req.toLowerCase())
    })
}