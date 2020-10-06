<script>
    export let category;
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
        background: rgb(7, 7, 197);
    }
    img {
        height: 16px;
        width: 16px;
        float: left;
    }
</style>

<button on:click class="category-link">
    <img src={category.image} alt="" />
    {category.name}</button>
