from flask import current_app

from artifice.scraper.redis import redis_client
from artifice.scraper.utils import cmp_dict


class Supervisor:
    '''
    Pseudo-object for accessing and modifying app state items.

    ENV development     ->  app.config, direct mutation
    ENV production      ->  Redis key-value store

    Default initial values are declared in config/constants.py
        and should be inherited by all config classes, allowing overrides.
    Used in conjunction with the defined schemas, which perform validations.

    # get current status of supervisor values
    >>> Supervisor.status()
    {
      "debug": False,
      "enabled": True,
      "polite": 10
    }

    >>> Supervisor.status(key="debug")
    False


    # pass validated data to modify with
    >>> data = schema.dump(request.get_json())
    >>> changed = Supervisor.handle_changes(data)
    {
    	"enabled": false,
    	"polite": 6
    }
    # NOTE: if validation was performed correctly,
    #       `changed` should be identical to `data`


    # render the changes in a human-readable manner
    >>> changed = Supervisor.handle_changes(data)
    >>> msg = Supervisor.render_msg(changed)
    [
      "enabled ==> False",
      "polite ==> 6"
    ]
    '''
    # # Functionality moved to @app.before_first_request
    # def __init__(self):
    #     from flask import current_app
    #     if current_app.env == 'production':
    #         keys = ['SUPERVISOR_ENABLED', 'SUPERVISOR_DEBUG', 'SUPERVISOR_POLITE']
    #         for key in keys:
    #             value = redis_client.get(key)
    #             if value is None:
    #                 default = current_app.config.get(key)
    #                 redis_client.set(key, default)


    @classmethod
    def status(cls, key=None):
        '''
        !! externally invoked method !!

        Displays all global app state values, aware of environment.
        By default, returns complete dict. Single values can be specifed.
        '''
        if current_app.env == 'production':
            src = redis_client
        else:
            src = current_app.config

        _enabled =  src.get('SUPERVISOR_ENABLED')
        _debug =    src.get('SUPERVISOR_DEBUG')
        _polite =   src.get('SUPERVISOR_POLITE')

        _dict = dict(enabled=_enabled, debug=_debug, polite=_polite)

        if key:
            return _dict.get(key)
        return _dict


    @classmethod
    def handle_changes(cls, data):
        '''
        !! externally invoked method !!
        '''
        before = cls.status()
        cls.set_enabled(data)
        cls.set_debug(data)
        cls.set_polite(data)
        after = cls.status()
        return cmp_dict(before, after)


    @staticmethod
    def render_msg(data):
        '''
        !! externally invoked method !!
        '''
        reply = []
        if not data:
            pass
        else:
            for k, v in data.items():
                reply.append('{0} ==> {1}'.format(k, v))
        return reply


    @classmethod
    def change(cls, key, value):
        '''
        Function by which all current_app config values are modified.
        '''
        if value is None:
            return

        key = cls.slugify(key)

        if current_app.env == 'production':
            redis_client.set(key, value)
        else:
            current_app.config[key] = value


    @classmethod
    def set_enabled(cls, data):
        key = 'enabled'
        value = data.get(key)
        cls.change(key, value)


    @classmethod
    def set_debug(cls, data):
        key = 'debug'
        value = data.get(key)
        cls.change(key, value)


    @classmethod
    def set_polite(cls, data):
        key = 'polite'
        value = data.get(key)
        cls.change(key, value)


    @staticmethod
    def slugify(key):
        '''
        before:    'enabled'
        after:      'SUPERVISOR_ENABLED'
        '''
        lowercase = ['supervisor', key]
        uppercase = [word.upper() for word in lowercase]
        return '_'.join(uppercase)
