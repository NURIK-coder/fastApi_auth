import datetime
from typing import Union, Optional

from pydantic import BaseModel, field_validator


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
    def parse_datea(cls, v):
        return v.strftime('%Y-%m-%d %H:%M')

