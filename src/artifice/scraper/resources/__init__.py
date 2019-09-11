from .base import api
from .index import IndexResource
from .health import HealthResource
from .document import DocumentsResource


api.add_resource(IndexResource, '/')
api.add_resource(HealthResource, '/health')
api.add_resource(DocumentsResource, '/documents/<int:document_id>', '/documents')
