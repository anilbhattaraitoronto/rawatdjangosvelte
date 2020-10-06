<script>
    export let productItem;
</script>

<style>
    .product {
        padding: 8px;
        box-shadow: 1px 1px 2px lightgray;
        width: 100%;
        max-width: 280px;
        margin: auto;
        line-height: 1.7;
        border-radius: 8px;
        text-align: center;
        cursor: pointer;
        transition: 300ms all ease-in-out;
    }
    .product:hover {
        box-shadow: 1px 2px 4px gray;
    }
    img {
        display: block;
        width: auto;
        height: 120px;
        padding: 8px;
        margin: auto;
        object-fit: cover;
    }
    .product-category {
        font-style: italic;
        font-weight: 400;
        letter-spacing: 1px;
    }
    button {
        all: unset;
        cursor: pointer;
        display: block;
        width: 100%;
        margin: 8px auto;
        text-align: center;
        color: yellow;
        background: rgb(106, 106, 156);

        padding: 4px 0;
        transition: 450ms all ease-in-out;
        border-radius: 20px;
    }
    button:hover {
        background: rgb(223, 223, 240);
        color: rgb(204, 143, 12);
    }
</style>

<div class="product" on:click>
    {#if productItem.image}<img src={productItem.image} alt="" />{/if}
    <h4 class="product-category">{productItem.category.name}</h4>
    <h3 class="product-name">{productItem.name}</h3>
    <p>Price: {productItem.price}</p>
    <p>Qty. {productItem.quantity}</p>
    <button class="add-to-cart" id={productItem.id}>Add to cart</button>
</div>
