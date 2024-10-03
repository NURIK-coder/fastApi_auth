

from sqlalchemy import Column, BigInteger, String

from app.base import Base


class User(Base):
    __tablename__ = 'users'
    id = Column(BigInteger, primary_key=True)
    username = Column(String(100), nullable=True, unique=True)
    password = Column(String(255), nullable=True)
    role = Column(String(20), default='user')

