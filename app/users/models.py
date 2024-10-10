import datetime

from sqlalchemy import Column, BigInteger, String, select, Text, TIMESTAMP, ForeignKey, UniqueConstraint
from sqlalchemy.orm import relationship, joinedload


from app.base import Base
from app.comment.models import Comment
from app.database import async_session_maker



class UserLikeComment(Base):
    __tablename__ = 'users_comments'
    id = Column(BigInteger, primary_key=True)
    user_id = Column(ForeignKey('users.id', ondelete='CASCADE'))
    comment_id = Column(ForeignKey(Comment.id, ondelete='CASCADE'))
    __table_args__ = (UniqueConstraint(user_id, comment_id, name='user_comment_uc'), )



class User(Base):
    __tablename__ = 'users'
    id = Column(BigInteger, primary_key=True)
    username = Column(String(100), nullable=True, unique=True)
    password = Column(String(255), nullable=True)
    role = Column(String(20), default='user')
    posts = relationship('Post', back_populates='user')
    comments = relationship('Comment', back_populates='user')
    liked_comments = relationship('Comment', secondary='users_comments', back_populates='users_liked')

    def __str__(self):
        return self.username

    @classmethod
    async def get_all(cls):
        async with async_session_maker() as session:
            query = select(cls).options(joinedload(cls.posts))
            result = await session.execute(query)
            return result.unique().scalars().all()

    @classmethod
    async def detail(cls, record_id: int):
        async with async_session_maker() as session:
            query = select(cls).filter_by(id=record_id).options(joinedload(cls.posts))
            result = await session.execute(query)
            return result.unique().scalar_one_or_none()

