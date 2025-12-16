import express from "express";

const PORT = 1245
const app = express()

const listProducts = [
  { id: 1, name: "Suitecase 250", price: 50, stock: 4 },
  { id: 2, name: "Suitecase 450", price: 100, stock: 10 },
  { id: 3, name: "Suitecase 650", price: 350, stock: 2 },
  { id: 4, name: "Suitecase 1050", price: 550, stock: 5 },
];
function getItemById(id) {
    const product = listProducts.find((product) => product.id === id) ;
    return product ? product : "Product not found."
}

app.get("/list_products", (req, res) => {
    res.json(listProducts);
});




app.listen(PORT, () => {
    console.log("Serveru running on 1245 PORT.")
})