from app.app_config.config import Config
from app.db.db_manager import DbManager
from app.models.user_models import UserRegister, LoginModel
from fastapi import APIRouter, HTTPException, Depends, Request

from app.models.user_profile_models import UserProfile
from app.utils.auth_token import create_access_token, get_current_user

router = APIRouter()
client = DbManager._get_client()
db = client[Config.MONGO_DB_NAME]
collection = db["user_register"]


@router.post("/user_register")
async def user_register(user: UserRegister):
    try:
        user_id = DbManager.add_user(user)
        return {"message": "Kullanıcı başarıyla eklendi.", "id": user_id}
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Kullanıcı eklenirken hata oluştu: {str(e)}")

@router.post("/login")
def user_login(login_user: LoginModel):
    user = collection.find_one({
        "kullanici_adi": login_user.username,
        "sifre": login_user.password
    })
    token = create_access_token({"sub": login_user.username})

    if not user:
        raise HTTPException(status_code=401, detail="Kullanıcı adı veya şifre hatalı")

    return {"message": "Giriş başarılı", "token": token}
@router.post("/profile/create")
def create_profile(profile: UserProfile, username: str = Depends(get_current_user)):
    profiles = db["user_profiles"]

    existing = profiles.find_one({"username": username})
    if existing:
        raise HTTPException(status_code=400, detail="Profil zaten var")

    profile_data = profile.dict()
    profile_data["username"] = username

    profiles.insert_one(profile_data)
    return {"message": "Profil başarıyla oluşturuldu"}
@router.get("/profile/me")
def get_my_profile(username: str = Depends(get_current_user)):

    profiles = db["user_profiles"]

    profile = profiles.find_one({"username": username})
    if not profile:
        raise HTTPException(status_code=404, detail="Profil bulunamadı")

    profile["_id"] = str(profile["_id"])
    return profile

