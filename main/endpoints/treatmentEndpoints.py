"""

"""
from flask import jsonify, request
from flask_restful import Resource
from main.models.treatment import Treatment


class TreatmentEndpoints(Resource):
    """
    
    """

    def __init__(self):
        """
        
        """
        self.treatment = Treatment()

    def get(self):
        """
        
        """
        data = request.get_json()
        if data:
            response = jsonify(self.treatment.select(data['filter']))
        else:
            response = jsonify(self.treatment.select())
        return response

    def post(self):
        """
        
        """
        data = request.get_json(force=True)
        response = jsonify(self.treatment.insert(data['body']))
        return response

    def put(self):
        """
        
        """
        data = request.get_json(force=True)
        response = jsonify(self.treatment.update(data['filter'], data['body']))
        return response

    def delete(self):
        """
        
        """
        data = request.get_json(force=True)
        response = jsonify(self.treatment.delete(data['filter']))
        return response
