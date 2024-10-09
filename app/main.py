from fastapi import FastAPI
from sqladmin import Admin

from app.admin import UserAdmin, PostAdmin
from app.database import engine

app = FastAPI()

from app.users.router import router as user_router
from app.posts.router import router as post_router

app.include_router(user_router)
app.include_router(post_router)

admin = Admin(app, engine, base_url='/admin')

admin.add_view(UserAdmin)
admin.add_view(PostAdmin)
