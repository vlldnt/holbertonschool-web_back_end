import { createClient, print } from "redis";

const client = createClient();

client.on("error", (err) => {
  console.log(`Redis client not connected to the server: ${err}`);
});

client.on("connect", () => {
  console.log("Redis client connected to the server");

  const schools = {
    Portland: 50,
    Seattle: 80,
    "New York": 20,
    Bogota: 20,
    Cali: 40,
    Paris: 2
  };

  // HSET HolbertonSchools with schools keys values object
  Object.entries(schools).forEach(([city, value]) => {
    client.HSET("HolbertonSchools", city, value, print);
  });

  client.HGETALL("HolbertonSchools", (err, object) => {
    if (err) {
      console.error(err);
      return;
    }
    console.log(object);
  });
});
