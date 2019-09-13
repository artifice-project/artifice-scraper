from flask import current_app

from artifice.scraper.utils import cmp_dict


class Supervisor:
    '''
    Pseudo-object for accessing and modifying app.config items.
    Values are declared in config/constants.py and inherited by all config classes.
    Used in conjunction with the defined schemas, which perform validations.

    # get current status of supervisor values
    >>> Supervisor.status()

        {
          "debug": false,
          "enabled": true,
          "polite": 10
        }


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

    @classmethod
    def status(cls):
        _enabled = current_app.config.get('SUPERVISOR_ENABLED')
        _debug = current_app.config.get('SUPERVISOR_DEBUG')
        _polite = current_app.config.get('SUPERVISOR_POLITE')
        return dict(enabled=_enabled, debug=_debug, polite=_polite)

    @classmethod
    def change(cls, key, desired, current=None):
        '''
        Function by which all current_app config values are modified.
        Function returns `1` if value is was_changed, else `0`
        Error raised if key is not an attribute of current_app.config
        '''
        if current is None:
            current_app.config[key] = desired
            was_changed = 1
        elif current_app.config.get(key) is current:
            current_app.config[key] = desired
            was_changed = 1
        elif current_app.config.get(key) is not current:
            was_changed = 0
        elif key not in current_app.config.keys():
            raise KeyError('`{0}` not in app.config, unable to set as `{1}`'.format(key, desired))
        return was_changed

    @classmethod
    def _enable(cls):
        key = 'SUPERVISOR_ENABLED'
        desired = True
        current = False
        was_changed = cls.change(key, desired, current)
        return was_changed

    @classmethod
    def _disable(cls):
        key = 'SUPERVISOR_ENABLED'
        desired = False
        current = True
        was_changed = Supervisor.change(key, desired, current)
        return was_changed

    @staticmethod
    def _debug_on():
        key = 'SUPERVISOR_DEBUG'
        desired = True
        current = False
        was_changed = Supervisor.change(key, desired, current)
        return was_changed

    @staticmethod
    def _debug_off():
        key = 'SUPERVISOR_DEBUG'
        desired = False
        current = True
        was_changed = Supervisor.change(key, desired, current)
        return was_changed

    @staticmethod
    def _polite(desired):
        '''
        Relies on schema to perform arg validation.
        Valid types are  { int, float }
        '''
        key = 'SUPERVISOR_POLITE'
        was_changed = Supervisor.change(key, desired)
        return was_changed

    @classmethod
    def set_enabled(cls, data):
        key = 'enabled'
        if data.get(key) is True:
            was_changed = cls._enable()
        elif data.get(key) is False:
            was_changed = cls._disable()
        else:
            was_changed = 0
        return was_changed

    @classmethod
    def set_debug(cls, data):
        key = 'debug'
        if data.get(key) is True:
            was_changed = cls._debug_on()
        elif data.get(key) is False:
            was_changed = cls._debug_off()
        else:
            was_changed = 0
        return was_changed

    @classmethod
    def set_polite(cls, data):
        key = 'polite'
        if data.get(key):
            desired = data.get(key)
            was_changed = cls._polite(desired)
        else:
            was_changed = 0
        return was_changed

    @classmethod
    def handle_changes(cls, data):
        before = cls.status()
        cls.set_enabled(data)
        cls.set_debug(data)
        cls.set_polite(data)
        after = cls.status()
        return cmp_dict(before, after)

    @staticmethod
    def render_msg(data):
        reply = []
        if not data:
            pass
        else:
            for k, v in data.items():
                reply.append('{0} ==> {1}'.format(k, v))
        return reply
