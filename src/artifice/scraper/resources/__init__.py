from .base import api
from .index import IndexResource
from .health import HealthResource
from .config import ConfigResource
from .status import StatusResource
from .metrics import MetricsResource
from .content import ContentResource
from .queue import QueueResource
from .echo import EchoResource


api.add_resource(IndexResource,     '/')
api.add_resource(HealthResource,    '/health')
api.add_resource(ConfigResource,    '/config')
api.add_resource(StatusResource,    '/status')
api.add_resource(MetricsResource,   '/metrics')
api.add_resource(QueueResource,     '/queue')
api.add_resource(EchoResource,      '/echo')
api.add_resource(ContentResource,   '/content', '/content/<int:content_id>')
