from sqlalchemy.orm import Session

from . import models, schemas


def get_has_category(db: Session, has_category_id: int):
    return db.query(models.Has_category).filter(models.Has_category.id_cat == has_category_id).first()


def get_has_category_by_value(db: Session, value: str):
    return db.query(models.Has_category).filter(models.Has_category.value == value).first()


def get_has_categorys(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Has_category).offset(skip).limit(limit).all()


def create_has_category(db: Session, has_category: schemas.Has_categoryCreate):
    db_has_category = models.Has_category(value=has_category.value)
    db.add(db_has_category)
    db.commit()
    db.refresh(db_has_category)
    return db_has_category


def get_newss(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.News).offset(skip).limit(limit).all()


def create_has_category_news(db: Session, news: schemas.NewsCreate, has_category_id: int):
    db_news = models.News(**news.dict(), owner_id=has_category_id)
    db.add(db_news)
    db.commit()
    db.refresh(db_news)
    return db_news

