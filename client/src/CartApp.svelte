<script>
    import { onMount } from "svelte";
    import CartBtn from "./cartComponents/CartBtn.svelte";
    import { products, cartProducts } from "./store/productStore.js";
    import CartProduct from "./cartComponents/CartProduct.svelte";

    let price;
    let qty = 1;

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
</style>

<h2 class="section-title">Cart</h2>

{#if $cartProducts}
    <article class="products">
        {#each $cartProducts as item}
            <CartProduct
                productItem={{ item, price: 2.99, qty }}
                on:click={() => removeItem(item.id)} />
        {/each}
    </article>
{:else}
    <p>No items in the cart yet</p>
{/if}
