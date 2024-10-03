from fastapi import FastAPI

app = FastAPI()

from app.users.router import router as main_router

app.include_router(main_router)