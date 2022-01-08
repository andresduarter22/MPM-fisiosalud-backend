from flask import Flask
from flask_restful import Api
from main.endpoints.patientEndponts import PatientEndpoints

class FisiosaludAPI(object):
    def __init__(self):
        self.app = Flask(__name__)
        api = Api(self.app)
        api.add_resource(PatientEndpoints, "/api/v1/patient", endpoint='patient')
        
    def run(self):
        self.app.run(debug=True)