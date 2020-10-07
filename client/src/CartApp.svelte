<script>
    import { onMount } from "svelte";
    import CartBtn from "./cartComponents/CartBtn.svelte";
    import {
        products,
        cartProducts,
        totalCartQuantity,
        totalCartPrice,
    } from "./store/productStore.js";
    import CartProduct from "./cartComponents/CartProduct.svelte";

    let productQuantity = 1;

    console.log("Cart Items are: ", $cartProducts);
    console.log(totalCartQuantity);

    // onMount(() => {
    //     fetch("store/api/products")
    //         .then((response) => response.json())
    //         .then((data) => {
    //             if (data.length > 0) {
    //                 $cartProducts = data[0];
    //             } else {
    //                 $cartProducts = [];
    //             }
    //         })
    //         .catch((err) => console.log("Error is: ", err));
    // });

    function removeItem(id) {
        $cartProducts = $cartProducts.filter((item) => item.id !== id);
        //adjust the total quantity and total cart price as products are removed
    }
    function updateQuantity(id) {
        console.log("id of updated quantity", id);
        //find the object
        let updatedProduct = $cartProducts.find((item) => item.id === id);
        $cartProducts = $cartProducts;
    }
</script>

<style>
    .section-title {
        color: rgb(9, 9, 94);
        background: rgb(221, 221, 233);
        font-size: 18px;
        padding: 8px 4px 8px 16px;
        letter-spacing: 2px;
        text-transform: uppercase;
        text-align: center;
    }
    .checkout-button {
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
    .checkout-button:hover {
        background: rgb(223, 223, 240);
        color: rgb(204, 143, 12);
    }
</style>

<h2 class="section-title">Cart</h2>

{#if $cartProducts.length > 0}
    <article class="products">
        {#each $cartProducts as item}
            <CartProduct
                productItem={item}
                on:click={() => removeItem(item.id)}
                on:change={() => updateQuantity(item.id)} />
        {/each}
    </article>
    <div class="cart-total-container">
        <p>Number of order items:{$totalCartQuantity}</p>
        <p>Total Cart Price: $ {$totalCartPrice}</p>
    </div>
    <div class="checkout-container">
        <button class="checkout-button">Checkout</button>
    </div>
{:else}
    <p>No items in the cart yet</p>
{/if}
