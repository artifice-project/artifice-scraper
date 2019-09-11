from flask import current_app
from flask import request, jsonify
from flask_restful import Resource


class HealthResource(Resource):
    def get(self):
        import git
        repo = git.Repo(search_parent_directories=True)
        sha = repo.head.object.hexsha
        env = current_app.config.get('ENV')
        return jsonify(sha=sha, env=env)
