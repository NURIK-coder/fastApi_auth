import datetime
from typing import Union, Optional, List

from pydantic import BaseModel, field_validator

from app.comment.schema import SComment


class SCPost(BaseModel):
    title: str  # Union[str, int]
    content: str  # Optional[str]
    likes_count: int

class SPost(BaseModel):
    id:int
    title: str
    likes_count:int
    created_at: datetime.datetime

    @field_validator('created_at')
    def parse_date(cls, v):
        return v.strftime('%Y-%m-%d %H:%M')


class SPostDetail(SPost):
    comments: List[SComment]