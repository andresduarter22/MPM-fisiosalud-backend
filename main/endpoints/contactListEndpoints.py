"""

"""
from flask import jsonify, request
from flask_restful import Resource
from main.models.contact_list import ContactList


class ContactListEndpoints(Resource):
    """
    
    """

    def __init__(self):
        """
        
        """
        self.contact = ContactList()

    def get(self):
        """
        
        """
        data = request.get_json()
        if data:
            response = jsonify(self.contact.select(data['filter']))
        else:
            response = jsonify(self.contact.select())

        return response

    def post(self):
        """
        
        """
        data = request.get_json(force=True)
        response = jsonify(self.contact.insert(data['body']))
        return response

    def put(self):
        """
        
        """
        data = request.get_json(force=True)
        response = jsonify(self.contact.update(data['filter'], data['body']))
        return response

    def delete(self):
        """
        
        """
        data = request.get_json(force=True)
        response = jsonify(self.contact.delete(data['filter']))
        return response
