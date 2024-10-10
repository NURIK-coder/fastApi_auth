import datetime

from sqlalchemy import Column, BigInteger, String, Text, Boolean, TIMESTAMP, insert, select, update, delete, ForeignKey
from sqlalchemy.orm import relationship, joinedload

from app.base import Base

from app.database import async_session_maker


class Category(Base):
    __tablename__ = 'categories'
    id = Column(BigInteger, primary_key=True)
    name = Column(String(100), nullable=False)
    posts = relationship('Post', back_populates='category')

    def __str__(self):
        return self.name

    @classmethod
    async def detail(cls, record_id: int):
        async with async_session_maker() as session:
            query = select(cls).filter_by(id=record_id).options(joinedload(cls.posts))
            result = await session.execute(query)
            return result.unique().scalar_one_or_none()



class Post(Base):
    __tablename__ = 'posts'
    id = Column(BigInteger, primary_key=True)
    title = Column(String(100), nullable=False)
    content = Column(Text)
    created_at = Column(TIMESTAMP, default=datetime.datetime.now)
    likes_count = Column(BigInteger, default=0)
    user_id = Column(BigInteger, ForeignKey('users.id', ondelete='CASCADE'))
    user = relationship('User', back_populates='posts')
    category_id = Column(BigInteger, ForeignKey('categories.id', ondelete='CASCADE'))
    category = relationship('Category', back_populates='posts')
    img = Column(String(255), nullable=True)
    comments = relationship('Comment', back_populates='post')

    def __str__(self):
        return self.title


    @classmethod
    async def get_all(cls):
        async with async_session_maker() as session:
            query = select(cls).options(joinedload(cls.user)).options(joinedload(cls.category))
            result = await session.execute(query)
            return result.scalars().all()

    @classmethod
    async def detail(cls, post_id):
        async with async_session_maker() as session:
            query = select(cls).filter_by(id=post_id).options(joinedload(cls.user)).options(joinedload(cls.comments))
            result = await session.execute(query)
            return result.unique().scalar_one_or_none()
