import datetime
import hashlib

from jose import jwt
from sqlalchemy import and_

from app.config import settings
from app.exeptions import IncorrectUsernameOrPassword
from app.users.models import User


def hash_password(password: str):
    return hashlib.sha256(password.encode('utf-8')).hexdigest()


async def authenticate_user(username: str, password: str):
    user = await User.find_one_or_none(filters=and_(User.username == username,
                                                    User.password == hash_password(password)))
    if user is None:
        raise IncorrectUsernameOrPassword

    return user

def create_access_token(data: dict):
    expire = datetime.datetime.now() + datetime.timedelta(hours=1)
    data['expire'] = expire.timestamp()
    token = jwt.encode(data, settings.SECRET_KEY, 'HS256')
    return token

