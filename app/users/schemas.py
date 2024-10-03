from pydantic import BaseModel


class SLogin(BaseModel):
    username: str
    password:str

class SRegister(BaseModel):
    username:str
    password:str

class SUser(BaseModel):
    id:int
    username: str
    role: str