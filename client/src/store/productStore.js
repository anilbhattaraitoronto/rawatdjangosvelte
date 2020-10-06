import { writable, derived } from "svelte/store";

export const products = writable(null);
export const cartProducts = writable(null);
