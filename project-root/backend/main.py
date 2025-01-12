from fastapi import FastAPI
from app.api.routes import register_routes

app = FastAPI()

app.include_router(register_routes.router, prefix="/api")