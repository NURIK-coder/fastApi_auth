from fastapi import FastAPI
from sqladmin import Admin

from app.admin import UserAdmin, PostAdmin, CategoryAdmin, CommentAdmin
from app.database import engine

app = FastAPI()

from app.users.router import router as user_router
from app.posts.router import router as post_router
from app.category.router import router as category_router
from app.comment.router import router as comment_router

app.include_router(user_router)
app.include_router(post_router)
app.include_router(category_router)
app.include_router(comment_router)

admin = Admin(app, engine, base_url='/admin')

admin.add_view(UserAdmin)
admin.add_view(PostAdmin)
admin.add_view(CategoryAdmin)
admin.add_view(CommentAdmin)
