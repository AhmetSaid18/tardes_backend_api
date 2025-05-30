class Config:
    MONGO_HOST = "localhost"  # MongoDB sunucusunun adresi
    MONGO_PORT = 27017        # MongoDB'nin portu
    MONGO_USER = "said"  # MongoDB kullanıcı adı
    MONGO_PASSWORD = "sifre"  # MongoDB şifresi
    MONGO_DB_NAME = "tardes"   # Veritabanı adı
    MONGO_URI = f"mongodb://{MONGO_USER}:{MONGO_PASSWORD}@{MONGO_HOST}:{MONGO_PORT}/{MONGO_DB_NAME}?authSource=admin"  # MongoDB URI'si