import { createClient, print } from "redis";

const client = createClient();

function setNewSchool(schoolName, value) {
  client.set(schoolName, value, print);
}

function displaySchoolValue(schoolName) {
  client.get(schoolName, (error, reply) => {
    console.log(reply);
  });
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
