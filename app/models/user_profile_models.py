from pydantic import BaseModel
from typing import Optional

class UserProfile(BaseModel):
    bio: Optional[str]
    favori_yemek: Optional[str]
    sehir: Optional[str]
    profil_foto_url: Optional[str]
