import os
from pymongo import MongoClient
from dotenv import load_dotenv
from datetime import datetime

# تحميل بيانات الرابط من ملف .env المخفي
load_dotenv()
uri = os.getenv("MONGO_URI")

def get_db_connection():
    try:
        client = MongoClient(uri)
        return client["Agina_Academy"]
    except Exception as e:
        print(f"Error connecting to Mango: {e}")
        return None

def log_activity(action, details):
    db = get_db_connection()
    if db is not None:
        logs = db["Activity_Logs"]
        log_entry = {
            "user": "agina2026",
            "action": action,
            "details": details,
            "timestamp": datetime.now()
        }
        result = logs.insert_one(log_entry)
        print(f"✅ تم تسجيل النشاط بنجاح: {action}")
        return result.inserted_id

if __name__ == "__main__":
    # تجربة بسيطة للتأكد من الاتصال
    log_activity("System Startup", "مشروع الأكاديمية بدأ العمل بنجاح")
