<script>
    import {
        products,
        cartProducts,
        totalCartPrice,
        categoryProducts,
    } from "../../store/productStore.js";
    import Product from "../shared/Product.svelte";

    export let params = {};
    products.subscribe((data) => {
        $categoryProducts = data.filter(
            (item) => item.category.slug == params.category
        );
        console.log($categoryProducts, params.category);
    });

    let cartProduct = {};
    function addToCart(id) {
        cartProduct = $products.find((item) => item.id === id);

        if ($cartProducts.length > 0) {
            //check if
            if ($cartProducts.find((item) => item.id == cartProduct.id)) {
                alert(
                    "Item already in cart. Please update quantity in the cart."
                );
                //show a modal
            } else {
                $cartProducts = [cartProduct, ...$cartProducts];
            }
        } else {
            $cartProducts = [cartProduct];
        }
    }
</script>

<h2 class="title is-capitalized">{params.category}</h2>

{#if $categoryProducts.length > 0}
    <!-- <h2 class="title has-text-centered">
    {#if productCategory.category.image}
        <img
            src={productCategory.category.image}
            alt=""
            class="category-image" />
    {/if}{productCategory.category.name}
</h2> -->
    <div class="columns is-multiline">
        {#each $categoryProducts as item (item.id)}
            <Product productItem={item} on:click={() => addToCart(item.id)} />
        {/each}
    </div>
{:else}
    <p>Click category Links to see category products</p>
{/if}
