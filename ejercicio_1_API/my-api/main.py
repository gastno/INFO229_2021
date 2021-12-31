from typing import List

from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from . import crud, models, schemas
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/has_category/", response_model=schemas.User)
def create_has_category(has_category: schemas.UserCreate, db: Session = Depends(get_db)):
    db_has_category = crud.get_has_category_by_value(db, value=has_category.value)
    if db_has_category:
        raise HTTPException(status_code=400, detail="Ya existe esa categoría")
    return crud.create_has_category(db=db, has_category=has_category)


@app.get("/has_category/", response_model=List[schemas.User])
def read_has_category(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    has_category = crud.get_has_category(db, skip=skip, limit=limit)
    return has_category


@app.get("/has_category/{has_category_id}", response_model=schemas.User)
def read_has_category(has_category_id: int, db: Session = Depends(get_db)):
    db_has_category = crud.get_has_category(db, has_category_id=has_category_id)
    if db_has_category is None:
        raise HTTPException(status_code=404, detail="No se encuentra noticia")
    return db_has_category


@app.post("/has_category/{has_category_id}/news/", response_model=schemas.News)
def create_item_for_has_category(
    has_category_id: int, item: schemas.NewsCreate, db: Session = Depends(get_db)
):
    return crud.create_has_category_item(db=db, item=item, has_category_id=has_category_id)


@app.get("/news/", response_model=List[schemas.News])
def read_news(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    news = crud.get_news(db, skip=skip, limit=limit)
    return news

