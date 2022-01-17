"""

"""
from flask import jsonify, request
from flask_restful import Resource
from main.models.document import Document


class DocumentEndpoints(Resource):
    """
    
    """

    def __init__(self):
        """
        
        """
        self.document = Document()

    def get(self):
        """
        
        """
        data = request.get_json()
        if data:
            response = jsonify(self.document.select(data['filter']))
        else:
            response = jsonify(self.document.select())
        return response

    def post(self):
        """
        
        """
        data = request.get_json(force=True)
        response = jsonify(self.document.insert(data['body']))
        return response

    def put(self):
        """
        
        """
        data = request.get_json(force=True)
        response = jsonify(self.document.update(data['filter'], data['body']))
        return response

    def delete(self):
        """
        
        """
        data = request.get_json(force=True)
        response = jsonify(self.document.delete(data['filter']))
        return response
