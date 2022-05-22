"""

"""
from flask import jsonify, request
from flask_restful import Resource
from main.middleware.authentication import token_required
from main.utils.string_utils import addObjectId, cleanBody

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
            filterClean = addObjectId({"_id": str(objectID)}, self.model.collection_name)
            response = jsonify(self.model.select(filterClean))
        else:
            response = jsonify(self.model.select())

        return response

    def post(self):
        """

        """
        data = request.get_json(force=True)
        bodyClean,_ = cleanBody(data['body'])
        print(bodyClean)
        response = jsonify(self.model.insert(bodyClean))
        return response

    def put(self):
        """

        """
        data = request.get_json(force=True)
        bodyClean, unset = cleanBody(data['body'])
        filterClean = addObjectId(data['filter'], self.model.collection_name)
        print("Unset", {'$unset': unset})
        response = jsonify(self.model.update(filterClean, bodyClean))
        return response

    def delete(self):
        """

        """
        data = request.get_json(force=True)
        filterClean = addObjectId(data['filter'], self.model.collection_name)
        response = jsonify(self.model.delete(filterClean))
        return response
