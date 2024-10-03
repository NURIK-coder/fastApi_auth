from typing import List

from fastapi import APIRouter, Depends

from app.users.auth import authenticate_user, create_access_token, hash_password
from app.users.dependencies import get_current_user
from app.users.models import User
from app.users.schemas import SLogin, SRegister, SUser

router = APIRouter(prefix='/user')


@router.get('/list')
async def user_list() -> List[SUser]:
    users = await User.get_all()
    return users

@router.post('/login')
async def login(data: SLogin):
    user = await authenticate_user(data.username, data.password)
    token = create_access_token({'sub': str(user.id)})

    return \
        {
            'access_token': token,
            'user': user
        }

@router.post('/register')
async def register(data:SRegister)-> SUser:
    user = await User.create(username=data.username, password=hash_password(data.password), role='user')
    return user

@router.post('/create')
async def create(user= Depends(get_current_user)):
    return 'success'

@router.delete('/delete/{user_id}')
async def delete_user(user_id: int):
    user = await User.delete(filters=User.id == user_id)
    return {'message':'User has been deleted'}

@router.get('/{user_id}')
async def get_user(user_id: int)->SUser:
    user = await User.detail(record_id=user_id)
    return user

