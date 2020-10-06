<script>
    import CartBtn from "./cartComponents/CartBtn.svelte";
    import { cartProducts } from "./store/productStore.js";
    import CartProduct from "./cartComponents/CartProduct.svelte";
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
        <CartProduct productItem={item} />
    {/each}
{:else}
    <p>No items in the cart yet</p>
{/if}
<CartBtn />
