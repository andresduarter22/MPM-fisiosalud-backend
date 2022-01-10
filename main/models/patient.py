"""
File that contains all functions related with the patient actions.
"""
from main.database_manager.db_manager import DbManager


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
           return DbManager.get_instance().select(self.collection_name, filter)
        except:
            print("ay nooooo")

    def insert(self, object):
        """
        
        """
        try:
            id = DbManager.get_instance().insertOne(self.collection_name, object)
            print(id)
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
        except:
            print("ay nooooo")
