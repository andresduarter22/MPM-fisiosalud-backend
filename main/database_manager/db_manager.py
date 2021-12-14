"""

"""
import json
import pprint
from pymongo import MongoClient
from collections import OrderedDict
from config import *
from main.utils.constants import collections


class DbManager:
    """
    
    """
    __instance = None
    
    def __init__(self):
        """
        
        """
        #TODO: put username and password
        self.client = MongoClient(host=DB_HOST_NAME, port=DB_PORT)
        # DB conection
        # db name
        self.db = self.client[DB_DATABASE]

    @staticmethod
    def get_instance():
        """
        This function gets a singleton instance of the DbManager class.
        Returns
        ----------
            DbManager: instance of DbManager class.
        """

        if DbManager.__instance is None:
            DbManager.__instance = DbManager()
        return DbManager.__instance
        
    def init_database(self):
        """
        
        """
        for collection in collections:
            self.db[collection].drop()
            self.db.create_collection(collection)
            with(open(f'main/schemas/{collection}_schema.json') as file):
                schema = json.load(file)
                cmd = OrderedDict([('collMod', collection),
                                   ('validator', schema),
                                   ('validationLevel', 'moderate')])
                self.db.command(cmd)

    def select(self, collectorName):
        """
        Select all elements on collection
        
        """
        response = []
        for element in self.db[collectorName].find():
            response.append(element)
            pprint.pprint(element)
        return response

    def insertOne(self, collectorName, element):
        """
        Insert one element on collection
        
        """
        return self.db[collectorName].insert_one(element)
        # print(f"One tutorial: {result.inserted_id}, {tutorial1}")

    def updateOne(self, collectorName, filter, element):
        """
        Update one element on collection
        
        """
        return self.db[collectorName].update_one(filter, {"$set": element})

    def deleteMany(self, collectorName, filter):
        """
        Delete many elements 
        
        """
        return self.db[collectorName].delete_many(filter)
