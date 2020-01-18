# all functions contained here are accessible at post-creation and pre-request
import logging
log = logging.getLogger(__name__)

def initialize_redis_store(keys):
    from flask import current_app
    if current_app.env == 'production':
        from artifice.scraper.redis import redis_client
        for key in keys:
            log.info("REDIS: Storing [{}] {}".format(key, type(key)))
            val = current_app.config.get(key)
            redis_client.set(key, val)
    else:
        pass
