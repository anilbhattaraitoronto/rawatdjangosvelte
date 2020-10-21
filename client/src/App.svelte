<script>
    import { onMount } from "svelte";
    import Router from "svelte-spa-router";
    import {
        products,
        categories,
        categoryProducts,
        cartProducts,
        totalCartQuantity,
        totalCartPrice,
    } from "./store/productStore.js";

    import Header from "./components/ui/Header.svelte";

    import Home from "./components/pages/Home.svelte";
    import Search from "./components/pages/Search.svelte";
    import Category from "./components/pages/Category.svelte";
    import ProductDetail from "./components/pages/ProductDetail.svelte";

    import CategoryLink from "./components/shared/CategoryLink.svelte";
    import Product from "./components/shared/Product.svelte";
    import CartProduct from "./cartComponents/CartProduct.svelte";

    const routes = {
        "/": Home,
        "/search": Search,
        "/categories/:category": Category,
        "/detail": ProductDetail,
    };
    //toggle menu in mobile size
    let is_active = false;

    function toggleMenu() {
        is_active == false ? (is_active = true) : (is_active = false);
    }

    // let categories = [];

    let productCategory = "";
    let cartProduct = {};

    onMount(() => {
        fetch("store/api/products")
            .then((response) => response.json())
            .then((data) => {
                if (data.length > 0) {
                    $products = data[0];
                    $categories = data[1];
                } else {
                    $products = [];
                }
            })
            .catch((err) => console.log("Error is: ", err));
    });
    function getCategoryProducts(category_slug) {
        products.subscribe((data) => {
            $categoryProducts = data.filter(
                (item) => item.category.slug == category_slug
            );
        });
        is_active == false ? (is_active = true) : (is_active = false);
    }

    function removeItem(id) {
        $cartProducts = $cartProducts.filter((item) => item.id !== id);
    }
    function updateQuantity(id) {
        //find the object
        let updatedProduct = $cartProducts.find((item) => item.id === id);
        $cartProducts = $cartProducts;
    }
</script>

<style>
    main {
        width: 100%;
        margin: auto;
    }

    .inCart {
        color: darkgreen;
    }
</style>

<nav class="navbar container is-fixed-top is-info p-2">
    <div class="navbar-brand">
        <a href="#/" class="navbar-item">
            <img src="/static/rawat_logo.png" alt="" />
        </a>
        <span
            class="navbar-burger burger {is_active == true ? 'is-active' : ''}"
            on:click={toggleMenu}>
            <span />
            <span />
            <span />
        </span>
    </div>
    <div class="navbar-menu {is_active == true ? 'is-active' : ''}">
        <div class="navbar-end">
            <a href="#/" class="navbar-item">Home</a>
            <a href="#/search" class="navbar-item">Search</a>
            <span class="navbar-item ">
                Cart:
                <strong class="{$cartProducts.length > 0 ? 'inCart' : ''} ">
                    $
                    {$totalCartPrice.toFixed(2)}</strong></span>
            <div class="navbar-item has-dropdown is-hoverable">
                <span class="navbar-link">Categories </span>
                {#if $categories.length > 0}
                    <div class="navbar-dropdown">
                        {#each $categories as category}
                            <a
                                href="#/categories/{category.slug}"
                                id={category.slug}
                                on:click={() => getCategoryProducts(category.slug)}
                                class=" navbar-item button is-small mt-1"><img
                                    src={category.image}
                                    alt=""
                                    width="16"
                                    height="16" />
                                {category.name}</a>
                        {/each}
                    </div>
                {/if}
            </div>
        </div>
    </div>
</nav>

<main class="section container">
    <div class="columns">
        <!-- BEGIN page column -->
        <div class="column">
            <Router {routes} />
        </div>
        <!-- END page column -->
        <!-- BEGIN - Cart column -->
        <article class=" column is-one-quarter">
            <h2
                class="title has-text-centered {$cartProducts.length > 0 ? 'inCart' : ''} ">
                Cart $
                {$totalCartPrice.toFixed(2)}
            </h2>

            {#if $cartProducts.length > 0}
                <article class="container is-flex is-flex-direction-column ">
                    {#each $cartProducts as item}
                        <CartProduct
                            productItem={item}
                            on:click={() => removeItem(item.id)}
                            on:change={() => updateQuantity(item.id)} />
                    {/each}
                </article>
                <div class="cart-total-container">
                    <p>Number of order items:{$totalCartQuantity}</p>
                    <p>Total Cart Price: $ {$totalCartPrice.toFixed(2)}</p>
                </div>
                <div class="checkout-container">
                    <button
                        class="button is-rounded is-primary">Checkout</button>
                </div>
            {:else}
                <p>No items in the cart yet</p>
            {/if}
        </article>
        <!-- End of card column -->
    </div>
    <!-- End of app columns container -->
</main>
