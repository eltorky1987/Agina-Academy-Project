import pymongo
import os
from datetime import datetime
from dotenv import load_dotenv

# تحميل المتغيرات من ملف .env لو موجود (عشان الترمكس)
load_dotenv()

# قراءة الرابط من البيئة (سواء .env أو GitHub Secrets)
uri = os.getenv("MONGO_URI")

def start_agina_engine():
    if not uri:
        print("❌ خطأ: مش لاقي رابط MONGO_URI. تأكد من ملف .env")
        return

    try:
        print("⏳ جاري إطلاق محرك أجينا والاتصال بالمانجو...")
        # استخدام إعدادات الاتصال اللي نجحت معانا قبل كدة
        client = pymongo.MongoClient(uri, serverSelectionTimeoutMS=30000)
        
        # التأكد من الاتصال (Ping)
        client.admin.command('ping')
        print("✅ تم تأكيد الاتصال.. السحابة جاهزة!")

        db = client["Agina_Academy"]
        col = db["Activity_Logs"]

        # تسجيل حركة تشغيل النظام
        status_update = {
            "event": "System Launch",
            "status": "Online 🔥",
            "device": "Termux_Main",
            "time": datetime.now()
        }

        col.insert_one(status_update)
        print("✅ تم إرسال إشارة التشغيل لقاعدة البيانات.")

    except Exception as e:
        print(f"❌ المانجو لسه معصلج: {e}")

if __name__ == "__main__":
    start_agina_engine()
