from fastapi import APIRouter
from app.schemas.item import ItemOut
from app.services.item_service import get_items

router = APIRouter()

@router.get("/", response_model=list[ItemOut])
def list_items():
    return get_items()
