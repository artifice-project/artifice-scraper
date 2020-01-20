from artifice.scraper.redis import redis_client
from artifice.scraper.utils import cmp_dict

import logging
log = logging.getLogger(__name__)

class Supervisor:
    '''
    Wrapper object for accessing and modifying app state items.

    Default initial values are declared in config/constants.py
    and should be inherited by all config classes, allowing overrides.
    Used in conjunction with the defined schemas, which perform validations.

    Operation is as follows:
        1. Current state is retrieved
        2. Schema performs load on args
        3. If any args pass validation, update
        4. New state is retrieved
        5. Changed values are formatted into msg
    '''
    @staticmethod
    def slugify(key):
        '''
        Converts friendly key names into slugified versions
        which are used as Redis & config keys.

        :param str key: lower-case key  (ex. `enabled`)
        :returns:       screaming snake (ex. `SUPERVISOR_ENABLED`)
        :rtype:         str
        '''
        lowercase = ['supervisor', key]
        uppercase = [word.upper() for word in lowercase]
        return '_'.join(uppercase)


    @classmethod
    def status(cls, key=None):
        '''
        Displays all global app state values, aware of environment.
        By default, returns complete dict. Single values can be specifed.
        '''
        # we could do this fancier, but this is dead-simple to debug
        _enabled =  redis_client.get('SUPERVISOR_ENABLED')
        _debug =    redis_client.get('SUPERVISOR_DEBUG')
        _polite =   redis_client.get('SUPERVISOR_POLITE')

        result = dict(enabled=_enabled, debug=_debug, polite=_polite)
        if key:
            return result[key]
        return result


    @classmethod
    def update(cls, marshallresult):
        """
        Takes in the result of schema.load() and updates the items.
        We take in the single `marshallresult` object because if the
        resulting dict is empty, an error would be raised on unpack.
        # TODO: unify how we are calling the SupervisorSchemas

        :param dict marshallresult: The result of schema.load(), can be {}
        :returns:                   Modified items
        :rtype:                     dict
        """
        before = cls.status()
        for key, val in marshallresult.items():
            slug = cls.slugify(key)
            log.info("Setting {} as {} to {}".format(key, slug, val))
            _ = redis_client.set(slug, val)
            log.debug("REDIS: {}".format(_))
        after = cls.status()
        changed = cmp_dict(before, after)
        return changed


    @staticmethod
    def render_msg(data):
        '''
        Takes in a dictionary (can be empty) of items which were updated
        and formats them as strings, showing what the values were changed to.
        '''
        reply = []
        if not data:
            pass
        else:
            for k, v in data.items():
                reply.append('{0} ==> {1}'.format(k, v))
        return reply
