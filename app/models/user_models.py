from pydantic import BaseModel


class UserRegister(BaseModel):
    kullanici_adi: str
    sifre: str
    dogum_tarihi: str
    cinsiyet: str
    sehir: str


class LoginModel(BaseModel):
    username:str
    password:str
