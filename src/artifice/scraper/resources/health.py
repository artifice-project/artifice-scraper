from flask import current_app
from flask import request, jsonify
from flask_restful import Resource

from artifice.etc.banners import artifice_version
from artifice.scraper.utils import (
    git_sha,
    time_of_deployment,
    is_service_running,
)

def percentify(arg):
    # param: arg:   int, float, str
    # returns: arg + '%'
    return '{}%'.format(arg)


class HealthResource(Resource):

    @staticmethod
    def systemctl(services):
        systemctl = {}
        for each in services:
            systemctl.update({each: is_service_running(each)})
        return systemctl

    @staticmethod
    def warnings(mem):
        '''
        Displays written warning messages if system resource usage rises
        above a predefined level. Right now this is just a simple workaround
        that allows for searching the /health endpoint data's `warning` field
        and feeding the information into a secondary source.
        '''
        msgs = []
        threshold = dict(
            cpu=75,
            ram=75,
            disk=75,
        )
        for key in threshold:
            if float(mem.get(key).split('%')[0]) > threshold.get(key):
                msg = '{} above threshold of {}%'.format(key.upper(), threshold.get(key))
                msgs.append(msg)
        return msgs

    @staticmethod
    def memory():
        import psutil
        from artifice.scraper.utils import disk_space_percent
        cpu_used_pct = psutil.cpu_percent()
        ram_used_pct = dict(psutil.virtual_memory()._asdict())['percent']
        disk_used_pct = disk_space_percent(path='/')
        return dict(
            cpu=percentify(cpu_used_pct),
            ram=percentify(ram_used_pct),
            disk=percentify(disk_used_pct),
        )

    def get(self):
        '''
        Displays information regarding the application.
        No mission-critical or secret data is shown,
        therefore no authentication is required to view.
        '''
        sha = git_sha()
        tod = time_of_deployment()
        env = current_app.config.get('ENV', '<None>')
        mem = self.memory()
        services = self.systemctl([
                        'celeryd',
                        'redis-server',
                        'postgresql',
                        ])
        ver = artifice_version()
        warns = self.warnings(mem)

        return jsonify(
            commit=sha,
            deployed=tod,
            environment=env,
            memory=mem,
            services={**services},
            version=ver,
            warnings=warns,
        )
