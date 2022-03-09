"""

"""
from flask import jsonify, request
from flask_restful import Resource, reqparse


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
        parser = reqparse.RequestParser()
        parser.add_argument('id', type=str)
        args = parser.parse_args()
        if data:
            response = jsonify(self.model.select(data['filter']))
        elif args.id:
            response = jsonify(self.model.select({"_id": str(args.id)}))
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
