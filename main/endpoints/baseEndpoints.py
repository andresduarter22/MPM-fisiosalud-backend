"""

"""
from flask import jsonify, request
from flask_restful import Resource


class BaseEndpoints(Resource):
    """

    """

    def __init__(self, model):
        """

        """
        self.model = model

    def get(self):
        """

        """
        data = request.get_json()
        if data:
            response = jsonify(self.model.select(data['filter']))
        else:
            response = jsonify(self.model.select())

        return response

    def post(self):
        """

        """
        data = request.get_json(force=True)
        response = jsonify(self.model.insert(data['body']))
        return response

    def put(self):
        """

        """
        data = request.get_json(force=True)
        response = jsonify(self.model.update(data['filter'], data['body']))
        return response

    def delete(self):
        """

        """
        data = request.get_json(force=True)
        response = jsonify(self.model.delete(data['filter']))
        return response
