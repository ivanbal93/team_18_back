from typing import Optional

from pydantic import BaseModel


class NewsCreate(BaseModel):
    title: str
    text: str
    url: str
    site_id: int
    views: Optional[int] = 0
    like: Optional[int] = 0
    repost: Optional[int] = 0

    class Config:
        orm_model = True


class NewsUpdate(BaseModel):
    title: Optional[str]
    text: Optional[str]
    is_favourite: Optional[bool] = False

    class Config:
        orm_model = True


class CommentCreate(BaseModel):
    text: str

    class Config:
        orm_model = True