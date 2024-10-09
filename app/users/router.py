import datetime
from typing import List

from fastapi import APIRouter, Depends, UploadFile, Form
from starlette.responses import Response

from app.posts.schemas import SPost
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
async def login(data: SLogin, response: Response):
    user = await authenticate_user(data.username, data.password)
    token = create_access_token({'sub': str(user.id)})
    response.set_cookie('token', token)

    return {'access_token': token,
            'user': user}


@router.post('/register')
async def register(username:str=Form(), password: str = Form()) -> SUser:
    user = await User.create(username=username, password=hash_password(password), role='user')
    return user




@router.delete('/delete/{user_id}')
async def delete_user(user_id: int):
    user = await User.delete(filters=User.id == user_id)
    return {'message': 'User has been deleted'}


@router.get('/current')
async def current(user: User = Depends(get_current_user)):
    return user



#
# @router.post('/create')
# async def create_post(file: UploadFile, user: User = Depends(get_current_user)):
#     fn = datetime.datetime.now().strftime('%Y-%m-%d %H-%M-%S') + '_'+file.filename
#     with open(f'media/posts/{fn}', 'wb') as f:
#         f.write(await file.read())
#     return 'success'




@router.get('/{user_id}')
async def get_user(user_id: int) -> SUser:
    user = await User.detail(record_id=user_id)
    return user
