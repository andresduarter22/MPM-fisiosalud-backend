"""

"""
from flask import jsonify, request
from flask_restful import Resource
from main.models.therapy import Therapy


class TherapyEndpoints(Resource):
    """
    
    """

    def __init__(self):
        """
        
        """
        self.therapy = Therapy()

    def get(self):
        """
        
        """
        data = request.get_json()
        if data:
            response = jsonify(self.therapy.select(data['filter']))
        else:
            response = jsonify(self.therapy.select())
        return response

    def post(self):
        """
        
        """
        data = request.get_json(force=True)
        response = jsonify(self.therapy.insert(data['body']))
        return response

    def put(self):
        """
        
        """
        data = request.get_json(force=True)
        response = jsonify(self.therapy.update(data['filter'], data['body']))
        return response

    def delete(self):
        """
        
        """
        data = request.get_json(force=True)
        response = jsonify(self.therapy.delete(data['filter']))
        return response
