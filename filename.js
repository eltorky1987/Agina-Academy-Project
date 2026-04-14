const { MongoClient, ServerApiVersion } = require('mongodb');

const username = encodeURIComponent("m2117513495_db_user");
const password = encodeURIComponent("YOUR_PASSWORD_HERE");

const uri = `mongodb+srv://${username}:${password}@cluster0.b2placb.mongodb.net/Agina_Academy?retryWrites=true&w=majority`;

const client = new MongoClient(uri, {
  serverApi: {
    version: ServerApiVersion.v1,
    strict: true,
    deprecationErrors: true,
  }
});

async function run() {
  try {
    console.log("⏳ جاري الاتصال...");

    await client.connect();

    await client.db("admin").command({ ping: 1 });

    console.log("✅ تم الاتصال بـ MongoDB بنجاح 🔥");

  } catch (err) {
    console.error("❌ خطأ:", err);
  } finally {
    await client.close();
  }
}

run();
