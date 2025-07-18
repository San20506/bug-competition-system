
// Shopping cart functionality
let cartItems = [];

function addToCart(productId) {
    // This function has bugs that need to be fixed
    cartItems.push({
        id: productId,
        name: "Product " + productId,
        price: 999
    });
    
    updateCartDisplay();
}

function updateCartDisplay() {
    const cartCount = cartItems.length;
    // This would update cart display
    console.log("Cart has " + cartCount + " items");
}
