<script>
    export let productItem;
</script>

<div class=" column is-4" on:click>
    <div class="card mx-1">
        {#if productItem.image}
            <div class="card-image">
                <figure class="image is-4by3">
                    <img src={productItem.image} alt="" />
                </figure>
            </div>
        {/if}
        <div class="card-content">
            <h4 class="product-category is-size-6">
                {productItem.category.name}
            </h4>
            <h3 class="product-name title is-size-5">{productItem.name}</h3>
            <p>Price: {productItem.price}</p>
            <p>Qty. {productItem.quantity}</p>
            <button
                class="button is-primary is-small is-rounded has-text-right"
                id={productItem.id}>Add to cart</button>
        </div>
    </div>
</div>
