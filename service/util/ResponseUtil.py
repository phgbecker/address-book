import json

from flask import Response


class ResponseUtil(object):

    @staticmethod
    def parse(result_set, show_dependencies=False):
        if result_set is not None:
            return Response(
                json.dumps(result_set, default=lambda a: a.to_dict(show_dependencies)), mimetype='application/json'
            )

        return Response(status=204)

    @staticmethod
    def parse_collection(result_set, show_dependencies=False):
        if len(result_set):
            return Response(
                json.dumps(result_set, default=lambda a: a.to_dict(show_dependencies)), mimetype='application/json'
            )

        return Response(status=204)
