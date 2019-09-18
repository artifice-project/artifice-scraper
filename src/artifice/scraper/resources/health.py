from flask import current_app
from flask import request, jsonify
from flask_restful import Resource

from artifice.etc.banners import artifice_version
from artifice.scraper.utils import (
    git_sha,
    time_of_deployment,
    is_service_running,
)


class HealthResource(Resource):

    def get(self):
        '''
        Displays information regarding the application.
        No mission-critical or secret data is shown,
        therefore no authentication is required to view.
        '''
        sha = git_sha()
        env = current_app.config.get('ENV')
        std = time_of_deployment()
        ver = artifice_version()
        services = {
            'celeryd': is_service_running('celeryd')
        }
        return jsonify(
            commit=sha,
            deployed=std,
            environment=env,
            version=ver,
            services={**services},
        )
