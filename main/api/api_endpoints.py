from flask import Flask
from flask_restful import Api
from main.endpoints.patientEndpoints import PatientEndpoints, PatientEndpointsByID
from main.endpoints.itemEndpoints import ItemEndpoints
from main.endpoints.shopArticleEndpoints import ShopArticleEndpoints
from main.endpoints.contactListEndpoints import ContactListEndpoints
from main.endpoints.staffEndpoints import StaffEndpoints
from main.endpoints.treatmentEndpoints import TreatmentEndpoints
from main.endpoints.workingAreaEndpoints import WorkingAreaEndpoints
from main.endpoints.therapyEndpoints import TherapyEndpoints
from main.endpoints.documentEndpoints import DocumentEndpoints
from main.database_manager.db_manager import DbManager


class FisiosaludAPI(object):
    def __init__(self):
        self.app = Flask(__name__)
        api = Api(self.app)
        self.addResources(api)

    def run(self):
        DbManager().init_database()
        self.app.run(debug=True)

    def addResources(self, api):
        api.add_resource(PatientEndpoints, "/api/v1/patient",
                         endpoint='patient')
        api.add_resource(ItemEndpoints, "/api/v1/item", endpoint='item')
        api.add_resource(TherapyEndpoints, "/api/v1/therapy",
                         endpoint='therapy')
        api.add_resource(TreatmentEndpoints,
                         "/api/v1/treatment", endpoint='treatment')
        api.add_resource(WorkingAreaEndpoints,
                         "/api/v1/workingArea", endpoint='workingArea')
        api.add_resource(DocumentEndpoints,
                         "/api/v1/document", endpoint='document')
        api.add_resource(ShopArticleEndpoints,
                         "/api/v1/shopArticle", endpoint='shopArticle')
        api.add_resource(ContactListEndpoints,
                         "/api/v1/contactList", endpoint='contactList')
        api.add_resource(StaffEndpoints, "/api/v1/staff",
                         endpoint='staff')
        api.add_resource(PatientEndpointsByID,
                         "/api/v1/patient/<string:patient_id>")
