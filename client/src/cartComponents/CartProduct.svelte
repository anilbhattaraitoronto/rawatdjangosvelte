<script>
    export let productItem;
    $: totalPrice = parseFloat(
        productItem.price * productItem.quantity
    ).toFixed(2);
</script>

<style>
    .product {
        /* padding: 8px; */
        box-shadow: 1px 1px 2px lightgray;
        width: 100%;
        max-width: 280px;
        margin: auto;
        text-align: center;
        background: rgb(236, 237, 238);
    }
    img {
        /* display: block;
        width: auto;
        height: 80px;
        padding: 8px;
        margin: auto; */
        object-fit: cover;
    }
    .product-category {
        font-style: italic;
        font-weight: 400;
        letter-spacing: 1px;
    }
    /* button {
        all: unset;
        cursor: pointer;
        display: block;
        width: 100%;
        margin: 8px auto;
        text-align: center;
        background: rgb(223, 223, 240);
        color: rgb(204, 143, 12);
        padding: 2px 0;
        transition: 450ms all ease-in-out;
        border-radius: 20px;
    }
    button:hover {
        color: rgb(9, 9, 94);
        background: rgb(221, 221, 233);
    } */
    label {
        display: block;
    }
    input {
        border-radius: 20px;
        width: 60px;
    }
</style>

<div class=" card mb-1">
    {#if productItem.image}
        <div class="card-image">
            <figure class="image is-4by3">
                <img src={productItem.image} alt="" width="auto" height="60" />
            </figure>
        </div>
    {/if}

    <div class="card-content">
        <h4 class="product-category">{productItem.category.name}</h4>
        <h3 class="product-name">{productItem.name}</h3>
        <p>Price: ${productItem.price}</p>
        <label>Qty.
            <input
                class="input"
                type="number"
                placeholder="quantity"
                min="1"
                bind:value={productItem.quantity}
                on:change />
        </label>
        <p>Total: ${totalPrice}</p>
    </div>

    <button
        on:click
        id={productItem.id}
        class="button is-small is-warning">Remove?</button>
</div>
