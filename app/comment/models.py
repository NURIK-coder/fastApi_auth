import datetime

from sqlalchemy import Column, BigInteger, Text, TIMESTAMP, ForeignKey, insert
from sqlalchemy.orm import relationship

from app.base import Base
from app.database import async_session_maker


class Comment(Base):
    __tablename__ = 'comments'
    id = Column(BigInteger, primary_key=True)
    text = Column(Text)
    created_at = Column(TIMESTAMP, default=datetime.datetime.now)
    post_id = Column(BigInteger, ForeignKey('posts.id', ondelete='CASCADE'))
    post = relationship('Post', back_populates='comments')
    user_id = Column(BigInteger, ForeignKey('users.id', ondelete='CASCADE'))
    user = relationship('User', back_populates='comments', foreign_keys=[user_id])
    users_liked = relationship('User', secondary='users_comments', back_populates='liked_comments')
    parent_id = Column(ForeignKey('comments.id', ondelete='CASCADE'))

    def __str__(self):
        return f'{self.user_id}'
