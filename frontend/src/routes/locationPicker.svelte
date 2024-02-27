
<script lang="ts">
    import { tick } from "svelte";


    import { location_completion, type location } from "./lcoation_search";
    import { browser } from "$app/environment";
    export var label:string

    export var onlocationchange:(loc:location)=>void


    export var placeholder:string|undefined = undefined




    var input:HTMLInputElement
    var completion : HTMLDivElement
    let options :location[] = []



    function on_input(){
        options = location_completion(input.value)
        completion.innerHTML = ""

        if (options.length == 1){
            pick_location(options[0])
        }

        for (let option of options){
            let div = document.createElement("p")
            div.innerHTML = option.name
            div.onclick = function(){
                pick_location(option)
            }
            completion.appendChild(div)   
        }
    }

    function pick_location(loc:location){
        input.value = loc.name
        onlocationchange(loc)
        completion.innerHTML = ""
        options = []
    }
    tick().then(()=>{
        if ( browser && placeholder != undefined){
            input.value=placeholder
            on_input()
        }
    })

</script>

<input type="text" id="locsearch" bind:this={input} on:input={on_input} on:blur={()=>options}>
<label for="locsearch">{label}</label>
<div bind:this={completion} class=completions style={"display:" + (options.length == 0 ? "none" : "block")}></div>

<p></p>
