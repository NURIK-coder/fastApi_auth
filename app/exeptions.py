from fastapi import HTTPException
from starlette import status

IncorrectUsernameOrPassword = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail='No user found with the given credentials'
)
NoToken = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail='Authontication credentail were not provided'
)
IncorrectToken = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail='Incorrect token format'
)

TokenExpired = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail='Token is expired'
)
