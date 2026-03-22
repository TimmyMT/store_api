from sqlalchemy import Column, Integer, String
from app.db import Base  # Base берём из db.py

class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    price = Column(Integer, nullable=False)
