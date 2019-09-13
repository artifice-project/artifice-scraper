from sqlalchemy import Column, String
from .base import db, BaseModel

class Queue(BaseModel):
    __tablename__ = 'queue'
    url =           Column(String(500), nullable=False, unique=True)
    status =        Column(String(10), nullable=False, default='READY')
