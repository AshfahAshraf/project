document.addEventListener("DOMContentLoaded", function(){

const products = {
potteryclayitems: ["Clay Pot", "Ceramic mugs" ,"Handmade plates","Decorative vases"],
HandloomTextile: ["Handloom Sarees", "Shawls", "Scarves", "Cushion cover"],
WoodenCraft: ["Wooden Toys", "Wall Decor", "Jewelry Boxes", "Key Holders"],
HandmadeJewelry : ["Beaded Necklaces", "Earrings", "Bangles", "Anklets"],
PaintingArtWork : ["Canvas paintings", "Wall Art", "Traditional Paintings", "Handmade Greeting Cards"],
BambooNaturalfiber :["Bambo Baskets", "Cane Chairs", "Mats", "Eco-friendly Decor"],
HomeLifestyle :["Scented Candles", "Handmade Soaps", "Photo Frames", "Macrame Wall Hangings"]
};

const category = document.getElementById("category");
const productDropdown = document.getElementById("productType");

category.addEventListener("change", function(){

let selected = this.value;

productDropdown.innerHTML = '<option value="">Select Product</option>';

if(products[selected]){

products[selected].forEach(function(product){

let option = document.createElement("option");
option.value = product;
option.textContent = product;

productDropdown.appendChild(option);

});

}

});

});
