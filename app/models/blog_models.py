from pydantic import BaseModel, validator, Field
from typing import List, Optional, Union
from datetime import datetime

class Comment(BaseModel):
    username: str
    comment: str
    timestamp: Optional[str]

class BlogModel(BaseModel):
    entry_title: str
    content: str
    hashtags: Union[str, List[str]]
    likes: Optional[List[str]] = Field(default_factory=list)
    dislikes: Optional[List[str]] = Field(default_factory=list)
    comments: Optional[List[Comment]] = Field(default_factory=list)

    @validator("hashtags", pre=True)
    def split_hashtags(cls, value):
        if isinstance(value, str):
            return [tag.strip() for tag in value.split(",")]
        return value
