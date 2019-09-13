import datetime
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from sqlachemy import Column, Integer, DateTime

migrate = Migrate()
db = SQLAlchemy()

class BaseModel(db.Model):
    __abstract__ = True
    id =            Column(Integer, nullable=False, unique=True, primary_key=True)
    created_at =    Column(DateTime(), nullable=False, default=datetime.datetime.utcnow())
    modified_at =   Column(DateTime(),nullable=True, onupdate=datetime.datetime.utcnow())
