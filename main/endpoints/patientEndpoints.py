"""

"""
from flask_restful import Resource
from flask import jsonify, request
from main.endpoints.baseEndpoints import BaseEndpoints
from main.models.patient import Patient


class PatientEndpoints(BaseEndpoints):
    """

    """

    def __init__(self):
        """

        """
        super().__init__(Patient())


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
