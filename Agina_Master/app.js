require('dotenv').config();

const express = require('express');
const mongoose = require('mongoose');

const app = express();

app.use(express.json());

// الاتصال بقاعدة البيانات
mongoose.connect(process.env.MONGO_URI)
.then(() => console.log("✅ MongoDB Connected"))
.catch(err => console.log("❌ Error:", err));

// اختبار السيرفر
app.get('/', (req, res) => {
  res.send("🔥 Agina Master Running");
});

app.listen(5000, () => {
  console.log("🚀 Server running on port 5000");
});
