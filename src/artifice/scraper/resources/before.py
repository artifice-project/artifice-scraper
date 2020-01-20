# all functions contained here are accessible at post-creation and pre-request
import logging
log = logging.getLogger(__name__)

def initialize_redis_store(**kwargs):
    from artifice.scraper.redis import redis_client
    for key, val in kwargs.items():
        log.info("REDIS: Key={} {}  Value={} {}".format(key, type(key), val, type(val)))
        _ = redis_client.set(key, val)
        log.debug("REDIS: {}".format(_))
