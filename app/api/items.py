from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.schemas.item import ItemCreate, ItemResponse, ItemUpdate
from app.services.item_service import create_item, get_items, get_item, update_item, delete_item
from app.db import SessionLocal

router = APIRouter(prefix="/items", tags=["Items"])

# зависимость для сессии
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=ItemResponse, status_code=status.HTTP_201_CREATED)
def create(item: ItemCreate, db: Session = Depends(get_db)):
    created_item = create_item(db, item)
    return created_item

@router.get("/", response_model=list[ItemResponse])
def index(db: Session = Depends(get_db)):
    items = get_items(db)
    return items

@router.get("/{item_id}", response_model=ItemResponse)
def show(item_id: int, db: Session = Depends(get_db)):
    item = get_item(db, item_id)
    return item

@router.put("/{item_id}", response_model=ItemResponse)
def update(item_id: int, item_data: ItemUpdate, db: Session = Depends(get_db)):
    item = update_item(db, item_id, item_data)
    return item

@router.delete("/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def destroy(item_id: int, db: Session = Depends(get_db)):
    delete_item(db, item_id)
    return None
