"""
File that contains all functions related with the staff actions.
"""
from main.database_manager.db_manager import DbManager
import hashlib


class Staff():
    """

    """

    def __init__(self):
        """

        """
        self.collection_name = "staff"

    def select(self, filter=None):
        """
        
        """
        # TODO: remove password, salt and pepper parameters from response
        try:
           return DbManager.get_instance().select(self.collection_name, filter)
        except:
            print("ay nooooo")

    def insert(self, object):
        """
        
        """
        try:
            hasher = hashlib.sha256()
            hasher.update(object["staff_password"].encode('utf-8'))
            object["staff_password"] = hasher.hexdigest()
            id = DbManager.get_instance().insertOne(self.collection_name, object)
            return self.select({"_id": id})
        except:
            print("ay nooooo")

    def update(self, filter, object):
        """
        
        """
        try:
            hasher = hashlib.sha256()
            hasher.update(object["staff_password"].encode('utf-8'))
            object["staff_password"] = hasher.hexdigest()
            return DbManager.get_instance().updateOne(self.collection_name, filter, object)
        except:
            print("ay nooooo")

    def delete(self, filter):
        """
        """
        if filter["_id"] == "0":
            return { "error": "You can't delete the admin user" }
        else: 
            try:
                DbManager.get_instance().delete(self.collection_name, filter)
            except:
                print("ay nooooo")
