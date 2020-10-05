<script>
    export let categoryLink;
</script>

<style>
    button {
        all: unset;
        display: block;
        width: 100%;
        margin: auto;
        padding: 4px;
        background: lightgray;
        color: darkblue;
    }
    .category-link {
        all: unset;
        padding: 4px 8px;
        margin: 2px 0;
        box-shadow: 0 1px 2px gray;
        font-weight: 300;
        transition: 300ms all ease-in-out;
    }
    .category-link:hover {
        color: white;
        background: rgb(6, 90, 116);
    }
</style>

<button on:click class="category-link">{categoryLink}</button>
