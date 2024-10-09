import datetime

from jose import jwt, JWTError
from starlette.requests import Request

from app.config import settings
from app.exeptions import NoToken, IncorrectToken, TokenExpired, IncorrectUsernameOrPassword
from app.users.models import User


async def get_current_user(request: Request):
    token = request.headers.get('Authorization')
    if token is None:
        token = request.cookies.get('token')

    if token is None:
        raise NoToken
    try:
        data = jwt.decode(token, settings.SECRET_KEY, 'HS256')
    except JWTError:
        raise IncorrectToken

    expire = data['expire']
    if expire < datetime.datetime.now().timestamp():
        raise TokenExpired

    user_id = data['sub']

    user = await User.find_one_or_none(filters=User.id == int(user_id))
    if user is None:
        raise IncorrectUsernameOrPassword

    return user
