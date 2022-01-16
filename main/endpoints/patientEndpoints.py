"""

"""
from flask import jsonify, request
from flask_restful import Resource
from main.models.patient import Patient


class PatientEndpoints(Resource):
    """

    """

    def __init__(self):
        """

        """
        self.patient = Patient()

    def get(self):
        """

        """
        data = request.get_json()
        if data:
            response = jsonify(self.patient.select(data['filter']))
        else:
            response = jsonify(self.patient.select())
        return response

    def post(self):
        """

        """
        data = request.get_json(force=True)
        response = jsonify(self.patient.insert(data['body']))
        return response

    def put(self):
        """

        """
        data = request.get_json(force=True)
        response = jsonify(self.patient.update(data['filter'], data['body']))
        return response

    def delete(self):
        """

        """
        data = request.get_json(force=True)
        response = jsonify(self.patient.delete(data['patient_id']))
        return response


class PatientEndpointsByID(Resource):
    """

    """

    def __init__(self):
        """

        """
        self.patient = Patient()
        self.id = {'_id': None}

    def get(self, patient_id):
        """

        """
        self.id['_id'] = patient_id
        response = jsonify(self.patient.select(self.id))
        return response

    def post(self, patient_id):
        """

        """
        self.id['_id'] = patient_id
        data = request.get_json(force=True)
        response = jsonify(self.patient.insert(data['body']))
        return response

    def put(self, patient_id):
        """

        """
        self.id['_id'] = patient_id
        data = request.get_json(force=True)
        response = jsonify(self.patient.update(self.id, data['body']))
        return response

    def delete(self, patient_id):
        """

        """
        self.id['_id'] = patient_id
        response = jsonify(self.patient.delete(self.id))
        return response
