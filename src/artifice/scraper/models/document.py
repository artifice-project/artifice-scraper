from sqlalchemy import Column, Integer
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.ext.mutable import MutableDict

from .base import db


class Document(db.Model):
    id = Column(Integer(), primary_key=True)
    data = Column(MutableDict.as_mutable(JSONB), nullable=False)

    def __init__(self, data):
        self.data = data

    def __repr__(self):
        return u'<Documents %s>'.format(self.id)

    def as_dict(self):
        data = {'id': self.id}
        data.update(self.data)
        return data
