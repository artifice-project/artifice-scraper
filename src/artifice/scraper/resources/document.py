import logging
from flask import request
from flask_restful import Resource
from werkzeug.exceptions import HTTPException

from artifice.scraper.models import Document


class NotFound(HTTPException):
    code = 404
    data = {}


class DocumentsResource(Resource):
    default_length = 100

    def get(self, document_id=None):
        if document_id:
            return self.get_one(document_id)
        return self.get_list()

    def get_one(self, document_id):
        document = Document.query.get(document_id)
        return document.as_dict()

    def get_list(self):
        query = self.paginate(Document.query)
        documents = [row.as_dict() for row in query]
        return documents

    def paginate(self, query):
        offset = int(request.args.get('start', 0))
        limit = int(request.args.get('length', self.default_length))
        if offset < 0 or limit < 0:
            raise NotFound()
        entries = query.limit(limit).offset(offset).all()
        if not entries:
            raise NotFound()

        return entries
