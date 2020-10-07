import { writable, derived } from "svelte/store";
let grandTotal;

export const products = writable([]);
export const cartProducts = writable([]);
export const totalCartQuantity = derived(
  cartProducts,
  (value) => value.reduce((acc, t) => acc + t.quantity, 0),
);
export const totalCartPrice = derived(
  cartProducts,
  ($cartProducts) =>
    $cartProducts.reduce((acc, t) => acc + t.price * t.quantity, 0),
);
