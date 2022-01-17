"""

"""
from flask import jsonify, request
from flask_restful import Resource
from main.models.working_area import WorkingArea


class WorkingAreaEndpoints(Resource):
    """
    
    """

    def __init__(self):
        """
        
        """
        self.workingArea = WorkingArea()

    def get(self):
        """
        
        """
        data = request.get_json()
        if data:
            response = jsonify(self.workingArea.select(data['filter']))
        else:
            response = jsonify(self.workingArea.select())
        return response

    def post(self):
        """
        
        """
        data = request.get_json(force=True)
        response = jsonify(self.workingArea.insert(data['body']))
        return response

    def put(self):
        """
        
        """
        data = request.get_json(force=True)
        response = jsonify(self.workingArea.update(data['filter'], data['body']))
        return response

    def delete(self):
        """
        
        """
        data = request.get_json(force=True)
        response = jsonify(self.workingArea.delete(data['filter']))
        return response
