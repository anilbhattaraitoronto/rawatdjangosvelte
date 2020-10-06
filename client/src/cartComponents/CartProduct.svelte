<script>
    export let productItem = {
        item,
        price: 2.99,
        qty: 1,
    };
    let totalPrice;

    $: totalPrice = (
        parseFloat(productItem.price.toFixed(2)) * parseInt(productItem.qty)
    ).toFixed(2);
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
        background: rgb(7, 7, 197);
        color: white;
        padding: 4px 0;
        transition: 450ms all ease-in-out;
        border-radius: 20px;
    }
    button:hover {
        color: rgb(9, 9, 94);
        background: rgb(221, 221, 233);
    }
    label {
        display: block;
    }
    input {
        border-radius: 20px;
        width: 80px;
    }
</style>

<div class="product">
    <h3>Cart Product</h3>
    {#if productItem.image}<img src={productItem.item.image} alt="" />{/if}
    <h4 class="product-category">{productItem.item.category.name}</h4>
    <h3 class="product-name">{productItem.item.name}</h3>
    <p>{productItem.price}</p>
    <label>Qty.
        <input
            type="number"
            placeholder="quantity"
            min="1"
            bind:value={productItem.qty} />
    </label>
    <p>{totalPrice}</p>
    <button>Remove Item</button>
</div>
