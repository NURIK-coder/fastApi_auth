from sqladmin import ModelView

from app.posts.models import Post
from app.users.models import User



class UserAdmin(ModelView, model=User):
    column_list = [User.username, User.role]
    form_columns = [User.username, User.role]
    icon = 'fa-solid fa-user-secret'

class PostAdmin(ModelView, model=Post):
    column_list = [Post.title, Post.likes_count]
    form_columns = [Post.title, Post.content, Post.likes_count]
    icon = 'fa-solid fa-signs-post'



