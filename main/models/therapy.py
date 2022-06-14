"""
File that contains all functions related with the therapy actions.
"""
from operator import contains
from main.database_manager.db_manager import DbManager
from bson.objectid import ObjectId
from main.utils.face_recon import delete_image, recognize_face, save_image, delete_image
from main.utils.constants import UNKNOWN_FACES_DIR
from main.models.patient import Patient


class Therapy():
    """

    """

    def __init__(self):
        """

        """
        self.collection_name = "therapy"

    def select(self, filter=None):
        """
        
        """
        if filter and not isinstance(filter["_id"], ObjectId):
            filter["_id"] = ObjectId(filter["_id"])
        try:
           return DbManager.get_instance().select(self.collection_name, filter)
        except:
            print("ay nooooo")

    def insert(self, object):
        """
        
        """
        try:
            id = DbManager.get_instance().insertOne(self.collection_name, object)
            return self.select({"_id": id})
        except Exception as e:
            print(e)

    def update(self, filter, object):
        """
        
        """
        if filter and not isinstance(filter["_id"], ObjectId):
            filter["_id"] = ObjectId(filter["_id"])
        try: 
            action_taken = object["action"]
            del object["action"]
            if "validate" in action_taken:
                if "face" in action_taken:
                    save_image(object["patient_image"],
                            "unknown_patient", UNKNOWN_FACES_DIR)
                    face_recon_response = recognize_face()
                    if face_recon_response["result"]:
                        del object["patient_image"]
                        DbManager.get_instance().updateOne(self.collection_name, filter, object)
                    delete_image(f"{UNKNOWN_FACES_DIR}/unknown_patient.jpg")
                    return face_recon_response
                elif "id" in action_taken:
                    patientInfo = Patient().select({"_id": object["patient_id"]})
                    if patientInfo:
                        del object['patient_id']
                        DbManager.get_instance().updateOne(self.collection_name, filter, object)
                        return patientInfo
                    else:
                        return {"result": False, "message": "Patient not found"}               
            elif action_taken == "cancel":
                object["therapy_status"] = "cancelled"
                DbManager.get_instance().updateOne(self.collection_name, filter, object)
                return {"result": True}
            elif action_taken == "update":
                return DbManager.get_instance().updateOne(self.collection_name, filter, object)

        except:
            print("Error updating therapy")

    def delete(self, filter):
        """
        
        """
        try:
            if '_id' in filter:
                filter["_id"] = ObjectId(filter["_id"])
                DbManager.get_instance().delete(self.collection_name, filter)
            else:
                DbManager.get_instance().delete(self.collection_name, filter)

        except:
            print("ay nooooo")
            