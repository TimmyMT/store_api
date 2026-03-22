from sqlalchemy.orm import Session
from app.models.item import Item
from app.schemas.item import ItemCreate, ItemUpdate

def create_item(db: Session, item_data: ItemCreate) -> Item:
    item = Item(name=item_data.name, price=item_data.price)
    db.add(item)
    db.commit()
    db.refresh(item)
    return item

def get_items_list(db: Session) -> list[Item]:
    return db.query(Item).all()

def get_item_by_id(db: Session, item_id: int) -> Item:
    return db.query(Item).filter(Item.id == item_id).one()

def update_item_by_id(db: Session, item_id: int, item_data: ItemUpdate) -> Item:
    item = get_item_by_id(db, item_id)
    item.name = item_data.name
    item.price = item_data.price
    db.commit()
    db.refresh(item)
    return item

def delete_item_by_id(db: Session, item_id: int) -> None:
    item = get_item_by_id(db, item_id)
    db.delete(item)
    db.commit()
