
<script lang="ts">

    import { location_completion, type location } from "./lcoation_search";
    export var label:string

    export var onlocationchange:(loc:location)=>void

    var input:HTMLInputElement
    var completion : HTMLDivElement
    let options :location[] = []

    function on_input(){
        options = location_completion(input.value)
        completion.innerHTML = ""
        for (let option of options){
            let div = document.createElement("p")
            div.innerHTML = option.name
            div.onclick = function(){
                input.value = option.name
                onlocationchange(option)
                completion.innerHTML = ""
                options = []
            }
            completion.appendChild(div)
        
        }
    }


</script>

<input type="text" id="locsearch" bind:this={input} on:input={on_input} on:blur={()=>options}>
<label for="locsearch">{label}</label>
<div bind:this={completion} class=completions style={"display:" + (options.length == 0 ? "none" : "block")}></div>

<p></p>
