import express from "express";
import redis from "redis";
import { promisify } from "util";

const PORT = 1245;
const app = express();
const client = redis.createClient();

const getAsync = promisify(client.get).bind(client);
const setAsync = promisify(client.set).bind(client);

client.on("connect", () => {
  console.log("Redis client connected to the server");
});

client.on("error", (err) => {
  console.log(`Redis client not connected to the server: ${err.message}`);
});

const listProducts = [
  { id: 1, name: "Suitcase 250", price: 50, stock: 4 },
  { id: 2, name: "Suitcase 450", price: 100, stock: 10 },
  { id: 3, name: "Suitcase 650", price: 350, stock: 2 },
  { id: 4, name: "Suitcase 1050", price: 550, stock: 5 },
];

function getItemById(id) {
  return listProducts.find((product) => product.id === id);
}

function reserveStockById(itemId, stock) {
  return setAsync(`item.${itemId}`, stock);
}

async function getCurrentReservedStockById(itemId) {
  const stock = await getAsync(`item.${itemId}`);
  return stock ? parseInt(stock) : null;
}

app.get("/list_products", (req, res) => {
  const products = listProducts.map((product) => ({
    itemId: product.id,
    itemName: product.name,
    price: product.price,
    initialAvailableQuantity: product.stock,
  }));
  res.json(products);
});

app.get("/list_products/:itemId", async (req, res) => {
  const itemId = parseInt(req.params.itemId);
  const product = getItemById(itemId);

  if (!product) {
    res.json({ status: "Product not found" });
    return;
  }

  const reservedStock = await getCurrentReservedStockById(itemId);
  const currentQuantity =
    reservedStock !== null ? product.stock - reservedStock : product.stock;

  res.json({
    itemId: product.id,
    itemName: product.name,
    price: product.price,
    initialAvailableQuantity: product.stock,
    currentQuantity,
  });
});

app.get("/reserve_product/:itemId", async (req, res) => {
  const itemId = parseInt(req.params.itemId);
  const product = getItemById(itemId);

  if (!product) {
    res.json({ status: "Product not found" });
    return;
  }

  const reservedStock = await getCurrentReservedStockById(itemId);
  const currentStock =
    reservedStock !== null ? product.stock - reservedStock : product.stock;

  if (currentStock < 1) {
    res.json({ status: "Not enough stock available", itemId });
    return;
  }

  const newReservedStock = reservedStock !== null ? reservedStock + 1 : 1;
  await reserveStockById(itemId, newReservedStock);
  res.json({ status: "Reservation confirmed", itemId });
});

app.listen(PORT, () => {
  console.log(`Server running on port ${PORT}`);
});
