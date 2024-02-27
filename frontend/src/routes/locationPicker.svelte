
<script lang="ts">
    import { type location } from "./lcoation_search";
    export var label:string
    export var placeholder:string
    export var onlocationchange:(loc:location)=>void

</script>

<input type="text" id="locsearch" {placeholder} on:input={e=>onlocationchange(e.target.value)}>
<label for="locsearch">{label}</label>

<p></p>
