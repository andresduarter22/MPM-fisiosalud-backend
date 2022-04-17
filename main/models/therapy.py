"""
File that contains all functions related with the therapy actions.
"""
from main.database_manager.db_manager import DbManager
from bson.objectid import ObjectId


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
        except:
            print("ay nooooo")

    def update(self, filter, object):
        """
        
        """
        if filter and not isinstance(filter["_id"], ObjectId):
            filter["_id"] = ObjectId(filter["_id"])
        try:
           return DbManager.get_instance().updateOne(self.collection_name, filter, object)
        except:
            print("ay nooooo")

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
