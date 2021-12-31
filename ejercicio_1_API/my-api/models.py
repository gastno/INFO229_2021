from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.sql.sqltypes import Date

from .database import Base #Se importa el objeto Base desde el archivo database.py

class News(Base): 

    __tablename__ = "news"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(20), unique=True, index=True)
    date = Column(Date)
    url = Column(String(100), unique=True, index=True)
    mediaoutlet = Column(String(20), unique=True, index=True)

    items = relationship("News", back_populates="has_category")

class Has_category(Base):

    __tablename__ = "has_category"

    id_cat = Column(Integer, primary_key=True, index=True)
    value = Column(String(20), unique=True, index=True)
    id_news = Column(Integer, ForeignKey("news.id"))

    owner = relationship("News", back_populates="items")
