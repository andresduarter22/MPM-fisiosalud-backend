import json
from flask import jsonify, request
from flask_restful import Resource
from main.models.patient import Patient

class PatientEndpoints(Resource):
    def __init__(self):
        self.patient = Patient()
        
    def get(self):
        data = request.get_json()
        response = jsonify(self.patient.select(data['filter']))
        return response

    def post(self):
        data = request.get_json(force=True)
        response = jsonify(self.patient.insert(data['body']))
        return response
    
    def put(self):
        data = request.get_json(force=True)
        response = jsonify(self.patient.update(data['filter'], data['body']))
        return response

    def delete(self):
        data = request.get_json(force=True)
        response = jsonify(self.patient.delete(data['patient_id']))
        return response
