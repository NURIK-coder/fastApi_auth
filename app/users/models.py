

from sqlalchemy import Column, BigInteger, String, select
from sqlalchemy.orm import relationship, joinedload

from app.base import Base
from app.database import async_session_maker


class User(Base):
    __tablename__ = 'users'
    id = Column(BigInteger, primary_key=True)
    username = Column(String(100), nullable=True, unique=True)
    password = Column(String(255), nullable=True)
    role = Column(String(20), default='user')
    posts = relationship('Post', back_populates='user')

    @classmethod
    async def get_all(cls):
        async with async_session_maker() as session:
            query = select(cls).options(joinedload(cls.posts))
            result = await session.execute(query)
            return result.scalars().all()

    @classmethod
    async def detail(cls, record_id: int):
        async with async_session_maker() as session:
            query = select(cls).filter_by(id=record_id).options(joinedload(cls.posts))
            result = await session.execute(query)
            return result.scalar_one_or_none()

