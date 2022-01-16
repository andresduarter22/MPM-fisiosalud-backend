"""

"""
from flask import jsonify, request
from flask_restful import Resource
from main.models.item import Item


class ItemEndpoints(Resource):
    """
    
    """

    def __init__(self):
        """
        
        """
        self.item = Item()

    def get(self):
        """
        
        """
        data = request.get_json()
        if data:
            response = jsonify(self.item.select(data['filter']))
        else:
            response = jsonify(self.item.select())
        return response

    def post(self):
        """
        
        """
        data = request.get_json(force=True)
        response = jsonify(self.item.insert(data['body']))
        return response

    def put(self):
        """
        
        """
        data = request.get_json(force=True)
        response = jsonify(self.item.update(data['filter'], data['body']))
        return response

    def delete(self):
        """
        
        """
        data = request.get_json(force=True)
        response = jsonify(self.item.delete(data['filter']))
        return response
