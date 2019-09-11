from flask import current_app
from flask import request, jsonify
from flask_restful import Resource
from operator import attrgetter


class IndexResource(Resource):

    @staticmethod
    def routes_command(sort='rule', all_methods=False):
        reply = []
        rules = list(current_app.url_map.iter_rules())
        if not rules:
            return reply
        ignored_methods = set(() if all_methods else ('HEAD', 'OPTIONS'))
        if sort in ('endpoint', 'rule'):
            rules = sorted(rules, key=attrgetter(sort))
        rule_methods = [','.join(sorted(rule.methods - ignored_methods)) for rule in rules]
        for rule, methods in zip(rules, rule_methods):
            if (rule.endpoint != 'static') and ('dashboard' not in rule.endpoint):
                reply.append(dict(endpoint=rule.endpoint, methods=methods.split(','), rule=rule.rule))
        return reply


    def get(self):
        routes = self.routes_command()
        return jsonify(routes)
