from .base import api
from .index import IndexResource
from .health import HealthResource
from .document import DocumentsResource
from .config import ConfigResource
from .status import StatusResource
from .metrics import MetricsResource
from .content import ContentResource
from .queue import QueueResource
from .beta import BetaResource

api.add_resource(IndexResource,     '/')
api.add_resource(HealthResource,    '/health')
api.add_resource(ConfigResource,    '/config')
api.add_resource(StatusResource,    '/status')
api.add_resource(MetricsResource,   '/metrics')
api.add_resource(ContentResource,   '/content')
api.add_resource(QueueResource,     '/queue')
api.add_resource(BetaResource,      '/beta')
api.add_resource(DocumentsResource, '/documents/<int:document_id>', '/documents')
