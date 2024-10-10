from sqladmin import ModelView

from app.posts.models import Post, Category
from app.users.models import User
from app.comment.models import Comment

class UserAdmin(ModelView, model=User):
    column_list = [User.username, User.role]
    form_columns = [User.username, User.role, User.password]
    icon = 'fa-solid fa-user-secret'

class PostAdmin(ModelView, model=Post):
    column_list = [Post.title, Post.likes_count]
    form_columns = [Post.title, Post.content, Post.likes_count, Post.category, Post.user, Post.user_id]
    icon = 'fa-solid fa-signs-post'


class CategoryAdmin(ModelView, model=Category):
    column_list = [Category.name]
    form_columns = [Category.name]
    icon = 'fa-solid fa-list'


class CommentAdmin(ModelView, model=Comment):
    column_list = [Comment.user]
    form_columns = [Comment.text, Comment.user, Comment.post]
    icon = 'fa-regular fa-comment'



