from typing import List

from pydantic import BaseModel

from app.posts.schemas import SPost


class SCategory(BaseModel):
    id: int
    name: str
    posts: List[SPost]