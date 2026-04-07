import pymongo
from datetime import datetime
import sys

# الرابط القوي اللي انت اخترته
uri = "mongodb://m2117513495_db_user:RTJfHzyzO6sDTG25@cluster0-shard-00-00.b2placb.mongodb.net:27017,cluster0-shard-00-01.b2placb.mongodb.net:27017,cluster0-shard-00-02.b2placb.mongodb.net:27017/Agina_Academy?ssl=true&replicaSet=atlas-9c4z2p-shard-0&authSource=admin&retryWrites=true&w=majority"

try:
    print("⏳ أجينا بيحاول يكلم السيرفر... اصبر عليه شوية")
    # زيادة وقت الانتظار لـ 45 ثانية عشان الترمكس والشبكة
    client = pymongo.MongoClient(uri, serverSelectionTimeoutMS=45000, connectTimeoutMS=45000)

    # اختبار الاتصال
    client.admin.command('ping')
    print("✅ أخيراً! السيرفر رد والاتصال شغال")

    db = client["Agina_Academy"]
    col = db["Activity_Logs"]

    data = {
        "status": "Working 🔥",
        "device": "Termux-Android",
        "time": datetime.now()
    }

    col.insert_one(data)
    print("✅ تم إرسال أول بيانات للسحابة بنجاح!")

except Exception as e:
    print("❌ لسه فيه مشكلة في الشبكة:")
    print(f"نوع الخطأ: {type(e).__name__}")
    print(f"التفاصيل: {e}")
    print("\n💡 نصيحة أجينا: جرب تقفل الواي فاي وتفتح بيانات الهاتف (Data) أو العكس وجرب تاني.")
