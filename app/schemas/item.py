from pydantic import BaseModel, PositiveInt

class ItemCreate(BaseModel):
    name: str
    price: PositiveInt

class ItemUpdate(BaseModel):
    name: str
    price: PositiveInt

class ItemResponse(BaseModel):
    id: int
    name: str
    price: int

    class Config:
        orm_mode = True
