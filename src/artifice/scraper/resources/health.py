from flask import current_app
from flask import request, jsonify
from flask_restful import Resource

from artifice.scraper.utils import git_sha

class HealthResource(Resource):
    def get(self):
        sha = git_sha()
        env = current_app.config.get('ENV')
        return jsonify(sha=sha, env=env)
