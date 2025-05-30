from app.models.blog_models import BlogModel
from app.app_config.config import Config
from dotenv import load_dotenv
from pymongo import MongoClient
import os
from datetime import datetime, time, date
from app.models.user_models import UserRegister

load_dotenv()
class DbManager:
    @staticmethod
    def _get_client():
        _host = os.getenv("MONGO_HOST")
        _port = os.getenv("MONGO_PORT")
        _username = os.getenv("MONGO_USER")
        _password = os.getenv("MONGO_PASSWORD")
        _database_name = os.getenv("MONGO_DB_NAME")

        # _mongo_uri = f"mongodb://{_username}:{_password}@{_host}:{_port}/{_database_name}?authSource=admin"
        _mongo_uri = os.getenv("MONGO_URI")
        # print(f"<<<<MONGO URI>>>>>: {_mongo_uri}")
        return MongoClient(_mongo_uri)

    @staticmethod
    def add_user(user: UserRegister):
        client = DbManager._get_client()
        db = client[Config.MONGO_DB_NAME]
        collection = db["user_register"]

        kullanici_dict = user.dict()


        sonuc = collection.insert_one(kullanici_dict)
        return str(sonuc.inserted_id)
    @staticmethod
    def save_to_blog(blog: BlogModel):
        client = DbManager._get_client()
        db = client[Config.MONGO_DB_NAME]
        collection = db["blog"]
        blogger_dict = blog.dict()
        result = collection.insert_one(blogger_dict)
        return str(result.inserted_id)

    @staticmethod
    def get_blog():
        client = DbManager._get_client()
        db = client[Config.MONGO_DB_NAME]
        collection = db["blog"]
        get_all_blog = collection.find()

        bloglar = []
        for blog in get_all_blog:
            blog["_id"] = str(blog["_id"])  # 🪄 ObjectId → string
            bloglar.append(blog)

        return bloglar

