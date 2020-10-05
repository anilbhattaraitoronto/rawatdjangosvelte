<script>
    import { onMount } from "svelte";
    import { products } from "./store/productStore.js";
    let categories = [];
    let categoryProducts = [];

    onMount(async () => {
        await fetch("store/api/products")
            .then((response) => response.json())
            .then((data) => {
                console.log("data is ", data);
                if (data.length > 0) {
                    $products = data[0];
                    categories = data[1];
                    console.log(
                        "Products and categories ",
                        $products,
                        categories
                    );
                } else {
                    $products = [];
                }
            })
            .catch((err) => console.log("Error is: ", err));
    });
    function getCategoryProducts(category_slug) {
        categoryProducts = [
            ...$products.filter((item) => item.category.slug === category_slug),
        ];
    }
</script>

<style>
    main {
        width: 100%;
        margin: auto;
    }

    nav {
        position: relative;
        display: flex;
        justify-content: end;
        align-items: center;
        background: rgb(6, 90, 116);
        color: white;
    }
    .nav-link {
        padding: 4px 4px 4px 16px;
    }
    .category-buttons {
        position: absolute;
        top: 28px;
        right: 0px;
        display: flex;
        flex-direction: column;
        text-align: right;
        transform: scale(0);
        transition: 300ms all ease-in-out;
        background: white;
        color: rgb(6, 90, 116);
    }
    #nav-list-button {
        display: block;
        cursor: pointer;
    }
    #nav-list-button:hover > .category-buttons {
        transform: scale(1);
    }
    .category-link {
        all: unset;
        padding: 4px 8px;
        margin: 2px 0;
        box-shadow: 0 1px 2px gray;
        font-weight: 300;
        transition: 300ms all ease-in-out;
    }
    .category-link:hover {
        color: white;
        background: rgb(6, 90, 116);
    }
    .products {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
        grid-gap: 4px;
    }
    .product {
        padding: 8px;
        box-shadow: 1px 2px 3px gray;
    }

    @media (min-width: 640px) {
        main {
            max-width: none;
        }
    }
</style>

<main>
    <nav>
        <a href="#" class="nav-link">Cart</a>
        <div id="nav-list-button">
            <span class="nav-link">Categories ▾</span>
            {#if categories.length > 0}
                <div class="category-buttons">
                    {#each categories as category}
                        <button
                            on:click={() => getCategoryProducts(category.slug)}
                            class="category-link">{category.name}</button>
                    {/each}
                </div>
            {/if}
        </div>
    </nav>
    <article class="category-product-container">
        <h2 class="section-title">Category Products</h2>
        {#if categoryProducts.length > 0}
            {#each categoryProducts as item (item.id)}
                <div class="product">
                    {#if item.image}<img src={item.image} alt="" />{/if}
                    <h4>{item.category.name}</h4>
                    <h3>{item.name}</h3>
                </div>
            {/each}
        {:else}
            <p>Click category Links to see category products</p>
        {/if}
    </article>
    <article id="product-container">
        <h2 class="section-title">New Products</h2>
        {#if $products}
            <div class="products">
                {#each $products as productItem (productItem.id)}
                    <div class="product">
                        {#if productItem.image}
                            <img src={productItem.image} alt="" />
                        {/if}
                        <h4 class="product-category">
                            {productItem.category.name}
                        </h4>
                        <h3 class="product-name">{productItem.name}</h3>
                        <button class="add-to-cart">Add to cart</button>
                    </div>
                {/each}
            </div>
        {:else}
            <p>No products yet...</p>
        {/if}
    </article>
</main>
