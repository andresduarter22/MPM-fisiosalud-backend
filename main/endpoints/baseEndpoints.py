"""

"""
from flask import jsonify, request
from flask_restful import Resource
from main.middleware.authentication import token_required

class BaseEndpoints(Resource):
    """

    """
    method_decorators = [token_required]

    def __init__(self, model):
        """

        """
        self.model = model

    def get(self):
        """

        """
        objectID = request.args.get('id')
        if objectID:
            response = jsonify(self.model.select({"_id": str(objectID)}))
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
