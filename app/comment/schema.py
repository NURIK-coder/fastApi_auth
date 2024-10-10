from pydantic import BaseModel


class SComment(BaseModel):
    id: int
    text: str
