import App from "./App.svelte";
import CartApp from "./CartApp.svelte";

const app = new App({
  target: document.getElementById("app"),
});

const cartApp = new CartApp({
  target: document.getElementById("cart"),
});
export default { app, cartApp };
