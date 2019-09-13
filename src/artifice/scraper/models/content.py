from sqlalchemy import Column, String, Text
from .base import db, BaseModel

class Content(BaseModel):
    __tablename__ = 'content'
    origin =        Column(String(500), unique=True, nullable=False)
    title =         Column(String(500))
    text =          Column(Text())
    captions =      Column(Text())
