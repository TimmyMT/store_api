from fastapi import FastAPI, HTTPException
from app.api import items

app = FastAPI()  # это объект приложения, как Rails.application

app.include_router(items.router, prefix="/items")
