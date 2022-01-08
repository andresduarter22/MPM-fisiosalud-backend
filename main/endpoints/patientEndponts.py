import json
from flask import jsonify, request
from flask_restful import Resource
from main.models.patient import Patient

class PatientEndpoints(Resource):
    def __init__(self):
        self.patient = Patient()
        
    def get(self):
        response = jsonify(self.patient.selectAll())
        return response

    def post(self):
        body = request.get_json(force=True)
        print(type(body))
        response = jsonify(self.patient.insert(body))
        print(type(response))
        return response
    
    def put(self, patient_id, body):

        response = jsonify(self.patient.update(patient_id, body))
        return response

    def delete(self, patient_id):
        response = jsonify(self.patient.delete(patient_id))
        return response
