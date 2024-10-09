import datetime

from sqlalchemy import Column, BigInteger, String, Text, Boolean, TIMESTAMP, insert, select, update, delete, ForeignKey
from sqlalchemy.orm import relationship, joinedload

from app.base import Base

from app.database import async_session_maker


class Category(Base):
    __tablename__ = 'categories'
    id = Column(BigInteger, primary_key=True)
    name = Column(String(100), nullable=False)
    post = relationship('Post', back_populates='category')

    @classmethod
    async def get_post_category(cls):
        async with async_session_maker() as session:
            query = select(cls).options(joinedload(cls.post))
            result = await session.execute(query)
            return result.scalars().all()


class Post(Base):
    __tablename__ = 'posts'
    id = Column(BigInteger, primary_key=True)
    title = Column(String(100), nullable=False)
    content = Column(Text)
    created_at = Column(TIMESTAMP, default=datetime.datetime.now)
    likes_count = Column(BigInteger, nullable=True)
    user_id = Column(BigInteger, ForeignKey('users.id', ondelete='CASCADE'))
    user = relationship('User', back_populates='posts')
    category_id = Column(BigInteger, ForeignKey('categories.id', ondelete='CASCADE'))
    category = relationship('Category', back_populates='post')

    @classmethod
    async def get_all(cls):
        async with async_session_maker() as session:
            query = select(cls).options(joinedload(cls.user))
            result = await session.execute(query)
            return result.scalars().all()

    @classmethod
    async def get_category_post(cls):
        async with async_session_maker() as session:
            query = select(cls).options(joinedload(cls.category))
            result = await session.execute(query)
            return result.scalars().all()