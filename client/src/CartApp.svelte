<script>
    import { onMount } from "svelte";
    import CartBtn from "./cartComponents/CartBtn.svelte";
    import { products, cartProducts } from "./store/productStore.js";
    import CartProduct from "./cartComponents/CartProduct.svelte";

    let price;
    let qty;

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
</script>

<style>
    .section-title {
        text-align: center;
        letter-spacing: 2px;
        text-transform: uppercase;
    }
</style>

<nav class="cart-nav">
    <h2 class="section-title">Cart</h2>
</nav>
{#if $cartProducts}
    {#each $cartProducts as item}
        <CartProduct productItem={{ item, price: 2.99, qty: 1 }} />
    {/each}
{:else}
    <p>No items in the cart yet</p>
{/if}
<CartBtn />
