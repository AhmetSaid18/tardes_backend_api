from bson import ObjectId
from datetime import datetime
from app.app_config.config import Config
from app.db.db_manager import DbManager
from app.models.blog_models import BlogModel, Comment
from fastapi import APIRouter, HTTPException, Depends, Request

from app.utils.auth_token import get_current_user

router = APIRouter()

@router.post("/blog_save")
async def user_register(blog: BlogModel):
    try:
        print("Blog verisi:", blog)
        saved_blog = DbManager.save_to_blog(blog)
        return {"message": "Blog başarıyla eklendi.", "blog_content": saved_blog}
    except Exception as e:
        print("🔥 Hata Detayı:", e)
        raise HTTPException(status_code=400, detail=f"Blog eklenirken hata oluştu: {str(e)}")
@router.get("/blog_get")
def get_all_blog():
    get_blog = DbManager.get_blog()
    return {"blogs": get_blog}
@router.post("/blog/{blog_id}/like")
def like_blog(blog_id: str, username: str = Depends(get_current_user)):
    blog_collection = DbManager._get_client()[Config.MONGO_DB_NAME]["blog"]

    blog = blog_collection.find_one({"_id": ObjectId(blog_id)})
    if not blog:
        raise HTTPException(status_code=404, detail="Blog bulunamadı")

    # Önce dislike'dan çıkar
    blog_collection.update_one({"_id": ObjectId(blog_id)}, {"$pull": {"dislikes": username}})
    # Like'a ekle (tekrarlı eklemesin)
    blog_collection.update_one({"_id": ObjectId(blog_id)}, {"$addToSet": {"likes": username}})

    return {"message": "Beğenildi"}
@router.post("/blog/{blog_id}/dislike")
def dislike_blog(blog_id: str, username: str = Depends(get_current_user)):
    blog_collection = DbManager._get_client()[Config.MONGO_DB_NAME]["blog"]

    blog = blog_collection.find_one({"_id": ObjectId(blog_id)})
    if not blog:
        raise HTTPException(status_code=404, detail="Blog bulunamadı")

    # Önce like'dan çıkar
    blog_collection.update_one({"_id": ObjectId(blog_id)}, {"$pull": {"likes": username}})
    # Dislike'a ekle
    blog_collection.update_one({"_id": ObjectId(blog_id)}, {"$addToSet": {"dislikes": username}})

    return {"message": "Beğenilmedi"}
@router.post("/blog/{blog_id}/comment")
def comment_blog(blog_id: str, comment: Comment, username: str = Depends(get_current_user)):
    blog_collection = DbManager._get_client()[Config.MONGO_DB_NAME]["blog"]

    if not blog_collection.find_one({"_id": ObjectId(blog_id)}):
        raise HTTPException(status_code=404, detail="Blog bulunamadı")

    yorum = {
        "username": username,
        "comment": comment.comment,
        "timestamp": datetime.utcnow().isoformat()
    }

    blog_collection.update_one({"_id": ObjectId(blog_id)}, {"$push": {"comments": yorum}})
    return {"message": "Yorum eklendi"}
