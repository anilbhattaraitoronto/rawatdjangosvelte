<script>
    import { onMount } from "svelte";
    import { products, cartProducts } from "./store/productStore.js";

    import CategoryLink from "./components/shared/CategoryLink.svelte";
    import Product from "./components/shared/Product.svelte";
    let categories = [];
    let categoryProducts = [];
    let productCategory = "";
    let cartProduct = {};

    onMount(() => {
        fetch("store/api/products")
            .then((response) => response.json())
            .then((data) => {
                if (data.length > 0) {
                    $products = data[0];
                    categories = data[1];
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

    function addToCart(id) {
        //Create a writable store called myCart
        //get product with selected id from $products and add it to $myCart
        //display $myCart onto the cart container
        //add quantity field (range or input field and bind the value to quantity)
        //create derived total for each product
        //create derived total for the whole cart
        //create reactive variable so that they adjust as customers adjust quantity of cart items
        //Checkout button should connect to backend through rest-api
        //
        console.log("Added productid to cart", id);
        console.log(typeof id);
        cartProduct = $products.find((item) => item.id === id);
        // console.log(cartProduct);
        // $cartProducts = [cartProduct];

        // console.log(cartProducts);
        if ($cartProducts) {
            $cartProducts = [cartProduct, ...$cartProducts];
        } else {
            $cartProducts = [cartProduct];
        }
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
        justify-content: flex-end;
        align-items: center;
        background: rgb(7, 7, 197);
        color: white;
        font-size: 18px;
    }
    nav .nav-link {
        padding: 8px 4px 8px 16px;
        color: white;
    }
    .category-buttons {
        position: absolute;
        top: 32px;
        right: 0px;
        display: flex;
        flex-direction: column;
        text-align: right;
        transform: scale(0);
        transition: 300ms all ease-in-out;
        background: white;
        color: rgb(7, 7, 197);
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
        grid-gap: 20px;
        justify-items: center;
        align-items: center;
    }
    .category-image {
        display: inline;
        width: auto;
        height: 40px;
        object-fit: cover;
        float: right;
        margin-right: 40px;
        border-radius: 3px;
    }
    .section-title {
        display: flex;
        justify-content: center;
        align-items: center;
        padding: 8px 0;
        background: rgb(252, 252, 250);
        margin: 20px 0;
        text-transform: uppercase;
        letter-spacing: 2px;
        word-spacing: 8px;
        font-size: 1.3em;
        box-shadow: 1px 2px 2px rgb(93, 95, 97);
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
                            {category}
                            on:click={() => getCategoryProducts(category.slug)} />
                    {/each}
                </div>
            {/if}
        </div>
    </nav>
    <article class="category-product-container">
        {#if categoryProducts.length > 0}
            <h2 class="section-title">
                {#if productCategory.category.image}
                    <img
                        src={productCategory.category.image}
                        alt=""
                        class="category-image" />
                {/if}{productCategory.category.name}
            </h2>
            <div class="products">
                {#each categoryProducts as item (item.id)}
                    <Product
                        productItem={item}
                        on:click={() => addToCart(item.id)} />
                {/each}
            </div>
        {:else}
            <p>Click category Links to see category products</p>
        {/if}
    </article>
    <article id="product-container">
        <h2 class="section-title">New Products</h2>
        {#if $products}
            <div class="products">
                {#each $products as productItem (productItem.id)}
                    <Product
                        {productItem}
                        on:click={() => addToCart(productItem.id)} />
                {/each}
            </div>
        {:else}
            <p>No products yet...</p>
        {/if}
    </article>
</main>
