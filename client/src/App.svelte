<script>
    import { onMount } from "svelte";
    import { products } from "./store/productStore.js";

    import CategoryLink from "./components/shared/CategoryLink.svelte";
    import Product from "./components/shared/Product.svelte";
    let categories = [];
    let categoryProducts = [];
    let productCategory = "";

    onMount(() => {
        fetch("store/api/products")
            .then((response) => response.json())
            .then((data) => {
                console.log("data is ", data);
                if (data.length > 0) {
                    $products = data[0];
                    categories = data[1];
                    console.log("Products ", $products);
                    console.log("categories", categories);
                } else {
                    $products = [];
                }
            })
            .catch((err) => console.log("Error is: ", err));
    });
    function getCategoryProducts(category_slug) {
        productCategory = $products.find(
            (item) => item.category.slug === category_slug
        );
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

    .products {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
        grid-gap: 4px;
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
                        <CategoryLink
                            categoryLink={category.name}
                            on:click={() => getCategoryProducts(category.slug)} />
                    {/each}
                </div>
            {/if}
        </div>
    </nav>
    <article class="category-product-container">
        {#if categoryProducts.length > 0}
            <h2 class="section-title">{productCategory.category.name}</h2>

            {#each categoryProducts as item (item.id)}
                <Product productItem={item} />
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
                    <Product {productItem} />
                {/each}
            </div>
        {:else}
            <p>No products yet...</p>
        {/if}
    </article>
</main>
