import pymongo
from urllib.parse import quote_plus
from datetime import datetime

# بياناتك الحقيقية مع التشفير السحري (quote_plus)
user = quote_plus("m2117513495_db_user")
password = quote_plus("RTJfHzyzO6sDTG25")

# الرابط "الصافي" بعد التعديل
uri = f"mongodb://{user}:{password}@cluster0-shard-00-00.b2placb.mongodb.net:27017,cluster0-shard-00-01.b2placb.mongodb.net:27017,cluster0-shard-00-02.b2placb.mongodb.net:27017/Agina_Academy?ssl=true&replicaSet=atlas-9c4z2p-shard-0&authSource=admin&retryWrites=true&w=majority"

def launch_agina_academy():
    try:
        print("⏳ جاري الاتصال بالرابط المشفر (Encoded URI)...")
        client = pymongo.MongoClient(uri, serverSelectionTimeoutMS=30000)
        
        # اختبار الاتصال (Ping)
        client.admin.command('ping')
        print("✅ أخيراً! الاتصال اشتغل تمام وبدون 'زفت أرور'")

        db = client["Agina_Academy"]
        col = db["Activity_Logs"]
        
        # تسجيل أول عملية ناجحة بأسلوب الـ Encode
        res = col.insert_one({
            "user": "eltorky1987",
            "status": "Encoded Connection 🔥",
            "time": datetime.utcnow()
        })
        print(f"✅ تم تسجيل البيانات بنجاح | ID: {res.inserted_id}")

    except Exception as e:
        print(f"❌ لسه فيه مشكلة (مستحيل بعد ده): {e}")

if __name__ == "__main__":
    launch_agina_academy()
