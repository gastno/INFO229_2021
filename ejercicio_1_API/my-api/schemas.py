from typing import List, Optional

from pydantic import BaseModel


class NewsBase(BaseModel):
    title: str
    description: Optional[str] = None


class NewsCreate(NewsBase):
    pass


class News(NewsBase):
    id: int
    owner_id: int

    class Config:
        orm_mode = True


class Has_categoryBase(BaseModel):
    mediaoutlet: str


class Has_categoryCreate(Has_categoryBase):
    value: str


class Has_category(Has_categoryBase):
    id: int
    is_active: bool
    items: List[News] = []

    class Config:
        orm_mode = True

