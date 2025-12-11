import { promisify } from "util";
import { createClient, print } from "redis";

const client = createClient();

function setNewSchool(schoolName, value) {
  client.set(schoolName, value, print);
}

async function displaySchoolValue(schoolName) {
  const getAsync = promisify(client.get).bind(client);
  const value = await getAsync(schoolName);
  console.log(value);
}

client.on("error", (err) => {
  console.log(`Redis client not connected to the server: ${err}`);
});

client.on("connect", () => {
  console.log("Redis client connected to the server");
});

displaySchoolValue("Holberton");
setNewSchool("HolbertonSanFrancisco", "100");
displaySchoolValue("HolbertonSanFrancisco");
