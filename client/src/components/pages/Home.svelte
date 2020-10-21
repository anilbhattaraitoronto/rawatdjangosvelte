<script>
    import {
        cartProducts,
        totalCartPrice,
        products,
    } from "../../store/productStore.js";
    import Banner from "../ui/Banner.svelte";
    import Product from "../shared/Product.svelte";
    let cartProduct = {};
    function addToCart(id) {
        cartProduct = $products.find((item) => item.id === id);
        if ($cartProducts.length > 0) {
            //check if
            if ($cartProducts.find((item) => item.id == id)) {
                alert(
                    "Item already in cart. Please update quantity in the cart."
                );
                //show a modal
            } else {
                $cartProducts = [cartProduct, ...$cartProducts];
                sessionStorage.setItem(
                    "cartProducts",
                    JSON.stringify($cartProducts)
                );
            }
        } else {
            $cartProducts = [cartProduct];
            sessionStorage.setItem(
                "cartProducts",
                JSON.stringify($cartProducts)
            );
        }
    }
</script>

<main>
    <Banner />
    {#if $products.length > 0}
        <h2 class="title has-text-centered">New Products</h2>
        <div class=" columns is-multiline p-2">
            {#each $products as productItem (productItem.id)}
                <Product
                    {productItem}
                    on:click={() => addToCart(productItem.id)} />
            {/each}
        </div>
    {:else}
        <p>No products yet...</p>
    {/if}
</main>
