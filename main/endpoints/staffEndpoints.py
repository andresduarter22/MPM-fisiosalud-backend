"""

"""
from flask import jsonify, request
from flask_restful import Resource
from main.models.staff import Staff


class StaffEndpoints(Resource):
    """
    
    """

    def __init__(self):
        """
        
        """
        self.staff = Staff()

    def get(self):
        """
        
        """
        data = request.get_json()
        if data:
            response = jsonify(self.staff.select(data['filter']))
        else:
            response = jsonify(self.staff.select())
        return response

    def post(self):
        """
        
        """
        data = request.get_json(force=True)
        response = jsonify(self.staff.insert(data['body']))
        return response

    def put(self):
        """
        
        """
        data = request.get_json(force=True)
        response = jsonify(self.staff.update(data['filter'], data['body']))
        return response

    def delete(self):
        """
        
        """
        data = request.get_json(force=True)
        response = jsonify(self.staff.delete(data['filter']))
        return response
