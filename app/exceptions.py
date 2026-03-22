from fastapi import HTTPException, status

class ItemNotFound(HTTPException):
    def __init__(self, detail: str = "Item not found"):
        super().__init__(status_code=status.HTTP_404_NOT_FOUND, detail=detail)
