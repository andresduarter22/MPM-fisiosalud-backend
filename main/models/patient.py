"""
File that contains all functions related with the patient actions.
"""
import shutil
from main.database_manager.db_manager import DbManager
from main.utils.constants import KNOWN_FACES_DIR
from main.utils.face_recon import save_patient_image

class Patient:
    """
    
    """

    def __init__(self):
        """
        
        """
        self.collection_name = "patient"

    def select(self, filter=None):
        """
        
        """
        try:
            response = DbManager.get_instance().select(self.collection_name, filter)
            return response
        except:
            print("ay nooooo")

    def insert(self, object):
        """
        
        """
        try:
            patient_image = object["patient_image"]
            save_patient_image(patient_image, object['patient_name'], object['_id'])
            del object["patient_image"]
            id = DbManager.get_instance().insertOne(self.collection_name, object)
            return self.select({"_id": id})
        except:
            print("ay nooooo")

    def update(self, filter, object):
        """
        
        """
        try:
            return DbManager.get_instance().updateOne(self.collection_name, filter, object)
        except:
            print("ay nooooo")

    def delete(self, filter):
        """
        """
        try:
            DbManager.get_instance().delete(self.collection_name, filter)
            shutil.rmtree(f"{KNOWN_FACES_DIR}/{filter['_id']}")
        except:
            print("ay nooooo")
