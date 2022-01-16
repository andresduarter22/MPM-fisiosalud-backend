"""
File taht contains all methods to interact with MongoDB.
"""
import json
from pymongo import MongoClient
from collections import OrderedDict
from config import *
from main.utils.constants import collections


class DbManager:
    """
    Class with all fucntions to comunicate woth the MongoDB database.
    """
    __instance = None

    def __init__(self):
        """
        This function contains the data to create the connection with the database.
        """
        #TODO: put username and password
        self.client = MongoClient(host=DB_HOST_NAME, port=DB_PORT)
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
        Function to initialize the database.
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

    def select(self, collectionName, filter=None):
        """
        Select all elements on collection.
        collectionName (string): Name of the colletion to use.
        filter (dict): parameters to filter the required elements.
        
        Returns
        ----------
            
        """
        response = []
        for element in self.db[collectionName].find(filter):
            if type(element['_id']) is not str:
                element['_id'] = str(element['_id'])
            response.append(element)
        return response

    def insertOne(self, collectionName, element):
        """
        Insert one element on collection.
        collectionName (string): Name of the colletion to use.
        element (dict): parameters to filter the required elements.
        
        Returns
        ----------

        """
        response = self.db[collectionName].insert_one(element)
        return response.inserted_id

    def updateOne(self, collectionName, filter, element):
        """
        Update one element on collection.
        collectionName (string): Name of the colletion to use.
        filter (string):
        element (dict):
        
        Returns
        ----------

        """
        response = self.db[collectionName].update_one(filter, {"$set": element})
        return response.raw_result

    def delete(self, collectionName, filter):
        """
        Delete all elements that match with the filter.
        collectionName (string): Name of the colletion to use.
        filter (string):
        
        Returns
        ----------

        """
        return self.db[collectionName].delete_many(filter)
