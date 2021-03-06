import os
from celery import Celery
from flask import Flask


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

config_variable_name = 'FLASK_CONFIG_PATH'
default_config_path = os.path.join(BASE_DIR, 'config', 'local.py')
os.environ.setdefault(config_variable_name, default_config_path)


def create_app(config_file=None, settings_override=None):
    '''
    Application factory for the Flask components.
    Extension initializations are performed via init_app()
    This is the function called via the `wsgi.py` module.
    '''
    app = Flask(__name__)

    if config_file:
        app.config.from_pyfile(config_file)
        config_source = config_file
    else:
        app.config.from_envvar(config_variable_name)
        config_source = os.environ[config_variable_name]

    from artifice.etc import terminal_output
    from termcolor import colored
    text = 'config_file:  {0}'.format(config_source)
    color = 'magenta'
    terminal_output(colored(text, color))

    if settings_override:
        app.config.update(settings_override)

    init_app(app)
    configure_logger(app)

    @app.before_first_request
    def do_before_first_request():
        """
        Functions registered here are NOT called at time of creation,
        but rather immediately before the first request is received.
        """
        keys = ['SUPERVISOR_ENABLED', 'SUPERVISOR_DEBUG', 'SUPERVISOR_POLITE']
        kwargs = dict.fromkeys(keys, None)
        for key in kwargs.keys():
            kwargs[key] = app.config[key]
        import artifice.scraper.resources.before as b4
        b4.initialize_redis_store(**kwargs)

    @app.before_request
    def do_before_request():
        # Called before EACH & EVERY REQUEST
        pass

    return app


def init_app(app):
    '''
    Initializes extentions. Pay attention to import order.
    '''
    from artifice.scraper.models import db, migrate
    db.init_app(app)
    migrate.init_app(app, db)
    from artifice.scraper.resources import api
    api.init_app(app)
    from artifice.scraper.schemas import ma
    ma.init_app(app)
    from artifice.scraper.redis import redis_client
    redis_client.init_app(app)
    if not app.env in ('testing', 'development'): # dashboard in production only
        import flask_monitoringdashboard as dashboard
        # dashboard.config.init_from(file='../config/dashboard.cfg')    # OR, env var
        dashboard.bind(app)
        # custom graphs...
        from artifice.scraper.utils.graphs import size_of_foo
        schedule = {'seconds': 30}
        dashboard.add_graph('Foo', lambda: size_of_foo(), **schedule)


def configure_logger(app):
    '''
    Configure the log handling for the Flask app.
    Celery logging is handled via artifice.scraper.tasks.run_celery()
    '''
    import sys
    import logging
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handlers = []
    if app.config.get('LOG_FILE'):
        file_handler = logging.FileHandler(filename=app.config['LOG_FILE'], mode='a')
        file_handler.setFormatter(formatter)
        handlers.append(file_handler)
    if app.debug:
        stream_handler = logging.StreamHandler(stream=sys.stdout)
        stream_handler.setFormatter(formatter)
        handlers.append(stream_handler)
    logging.basicConfig(
        datefmt='%m/%d/%Y %I:%M:%S %p',
        level=getattr(logging, app.config.get('LOG_LEVEL', 'INFO')),
        handlers=handlers
    )
    # Adjust logging level on a per-module basis
    logging.getLogger('apscheduler').setLevel(logging.WARNING)


def create_celery_app(app=None):
    '''
    Application factory for the Celery components.
    Workers are started via artifice.scraper.tasks.run_celery()
    '''
    app = app or create_app()
    celery = Celery(
        app.name,
        broker=app.config['CELERY_BROKER_URL'],
        include=app.config['CELERY_INCLUDE'],
        backend=app.config['CELERY_BACKEND'],
    )
    celery.conf.update(app.config)
    TaskBase = celery.Task

    class ContextTask(TaskBase):
        '''
        Generic class which allows called tasks to be bound to app context.
        '''
        abstract = True

        def __call__(self, *args, **kwargs):
            with app.app_context():
                return TaskBase.__call__(self, *args, **kwargs)

    celery.Task = ContextTask
    return celery
