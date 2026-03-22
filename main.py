from fastapi import FastAPI, HTTPException
from fastapi.exceptions import RequestValidationError
from sqlalchemy.orm.exc import NoResultFound
from fastapi.responses import JSONResponse
from app.api import items

app = FastAPI()

@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request, exc):
    return JSONResponse(
        status_code=400,
        content={"detail": exc.errors()},
    )

@app.exception_handler(NoResultFound)
async def no_result_found_handler(request: Request, exc: NoResultFound):
    return JSONResponse(
        status_code=404,
        content={"detail": "Item not found"},
    )

app.include_router(items.router)
