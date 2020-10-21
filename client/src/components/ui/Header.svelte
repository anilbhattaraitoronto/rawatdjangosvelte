<script>
    import {
        totalCartPrice,
        cartProducts,
        categories,
    } from "../../store/productStore.js";
    export let is_active;
</script>

<nav class="navbar is-fixed-top is-info">
    <div class="navbar-brand">
        <a href="#/" class="navbar-item">
            <img src="/static/rawat_logo.png" alt="" />
        </a>
        <span
            class="navbar-burger burger {is_active == true ? 'is-active' : ''}"
            on:click>
            <span />
            <span />
            <span />
        </span>
    </div>
    <div class="navbar-menu {is_active == true ? 'is-active' : ''}">
        <div class="navbar-end">
            <a href="#/" class="navbar-item">Home</a>
            <a href="#/search" class="navbar-item">Search</a>
        </div>
    </div>
</nav>

<nav class="navbar">
    <span class="nav-cart-detail ">
        <b>CART:</b>
        <strong class="{$cartProducts.length > 0 ? 'inCart' : ''} ">
            $
            {$totalCartPrice.toFixed(2)}</strong></span>
    <div id="nav-list-button">
        <span class="nav-link">Categories ▾</span>
        {#if $categories.length > 0}
            <div class="category-buttons">
                {#each $categories as category}
                    <a
                        href="#/categories/{category.slug}"
                        id={category.slug}
                        on:click
                        class="button is-link is-small mt-1"><img
                            src={category.image}
                            alt=""
                            width="16"
                            height="16" />
                        {category.name}</a>
                {/each}
            </div>
        {/if}
    </div>
</nav>
