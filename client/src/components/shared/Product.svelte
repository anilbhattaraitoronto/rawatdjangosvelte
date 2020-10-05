<script>
    export let productItem;
</script>

<style>
    .product {
        padding: 8px;
        box-shadow: 1px 2px 3px gray;
    }
</style>

<div class="product">
    {#if productItem.image}<img src={productItem.image} alt="" />{/if}
    <h4 class="product-category">{productItem.category.name}</h4>
    <h3 class="product-name">{productItem.name}</h3>
    <button class="add-to-cart">Add to cart</button>
</div>
