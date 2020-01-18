from .base import ma, BaseArgSchema, PaginationSchema
from .args import QueueArgsSchema
from .status import StatusSchema
from .queue import QueueSchema
from .content import ContentSchema

status_schema        = StatusSchema()
queue_schema         = QueueSchema()
queues_schema        = QueueSchema(many=True)
queue_task_schema    = QueueSchema(only=('status','url'))
queues_task_schema   = QueueSchema(many=True, only=('status','url'))
content_schema       = ContentSchema()
contents_schema      = ContentSchema(many=True)
args_schema          = BaseArgSchema()
queue_args_schema    = QueueArgsSchema()
pagination_schema    = PaginationSchema()
