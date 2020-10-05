<script>
    export let productItem;
</script>

<style>
    .product {
        padding: 8px;
        box-shadow: 1px 2px 3px gray;
        width: 100%;
        max-width: 280px;
        margin: auto;
    }
    img {
        display: block;
        width: 60%;
        max-width: 180;
        height: 240px;
        margin: auto;
        object-fit: cover;
    }
</style>

<div class="product">
    {#if productItem.image}<img src={productItem.image} alt="" />{/if}
    <h4 class="product-category">{productItem.category.name}</h4>
    <h3 class="product-name">{productItem.name}</h3>
    <button class="add-to-cart">Add to cart</button>
</div>
