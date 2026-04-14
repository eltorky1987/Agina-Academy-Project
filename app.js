const { MongoClient, ServerApiVersion } = require('mongodb');

const username = "m2117513495_db_user";
const password = encodeURIComponent("RTJfHzyzO6sDTG25");

const uri = `mongodb+srv://${username}:${password}@cluster0.b2placb.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0`;

const client = new MongoClient(uri, {
  serverApi: {
    version: ServerApiVersion.v1,
    strict: true,
    deprecationErrors: true,
  }
});

async function run() {
  try {
    await client.connect();
    await client.db("admin").command({ ping: 1 });
    console.log("✅ Connected to MongoDB successfully!");
  } catch (err) {
    console.error("❌ Error:", err);
  } finally {
    await client.close();
  }
}

run();





