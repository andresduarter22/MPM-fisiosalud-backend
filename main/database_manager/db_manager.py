"""
File taht contains all methods to interact with MongoDB.
"""
import json
from pprint import pprint
import random
import hashlib
from pymongo.mongo_client import MongoClient
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
        tries = 0
        while tries < 10:
            try:
                tries += 1
                self.client = MongoClient(host=DB_HOST_NAME, port=DB_PORT)
                self.client.admin.command('ping')
            except Exception:
                print("Cannot reach the database, retrying")
                continue
            break
        
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
        created = False
        existing_collections = self.db.list_collection_names()
        for collection in collections:
            # if collection exists, do not create it again
            if collection in existing_collections:
                created = True
                continue
            self.db[collection].drop()
            self.db.create_collection(collection)
            with(open(f'main/schemas/{collection}_schema.json') as file):
                schema = json.load(file)
                cmd = OrderedDict([('collMod', collection),
                                   ('validator', schema),
                                   ('validationLevel', 'moderate')])
                self.db.command(cmd)

        # create admin account
        if not created:
            self.create_default_data()
    
    def create_default_data(self):
                # letters = string.ascii_lowercase
        # admin_pass = ''.join(random.choice(letters) for _ in range(32))
        admin_pass = 'ukfcbyzbrvkpdigospyvepzrzluxizcf1'
        hasher = hashlib.sha256()
        hasher.update(admin_pass.encode('utf-8'))
        print("Initial admin password: ", admin_pass.encode('utf-8'),
                "change this as soon as possible")
        self.insertOne("staff", {
            "_id": "0",
            "staff_name": "admin",
            "staff_phone_number": "7200098",
            "staff_email": "andres@gmail.com",
            "staff_role": "admin",
            "staff_password": hasher.hexdigest()
        })
        area = self.insertOne("workingArea", {
            "area_name": "Fisioterapia",
            "area_total_capacity": 12,
            "area_available": True
        })
        patient = self.insertMany("patient", [{"_id": "0",
            "patient_name": "andres",
            "patient_email": "andres@gmail.com",
            "patient_nickname": "dinis",
            "patient_birthday": "01/01/2000",
            "patient_phone_number": "7200098",
            "patient_address": "calle G # 111 Achumani",
            "reference_contact_name" : "andres",
            "reference_contact_number": "7200098"}, {"_id": "1",
            "patient_name": "jose",
            "patient_email": "jose@gmail.com",
            "patient_nickname": "jose",
            "patient_birthday": "01/01/2000",
            "patient_phone_number": "7200090",
            "patient_address": "calle G # 111 Achumani",
            "reference_contact_name" : "andres",
            "reference_contact_number": "7200098"},{"_id": "2",
            "patient_name": "luis",
            "patient_email": "luis@gmail.com",
            "patient_nickname": "JL",
            "patient_birthday": "01/01/2000",
            "patient_phone_number": "7200009",
            "patient_address": "calle G # 108 Achumani",
            "reference_contact_name" : "andres",
            "reference_contact_number": "7200098"},{"_id": "3",
            "patient_name": "maria",
            "patient_email": "maria@gmail.com",
            "patient_nickname": "mag",
            "patient_birthday": "01/01/2000",
            "patient_phone_number": "7205098",
            "patient_address": "calle H # 19 Achumani",
            "reference_contact_name" : "andres",
            "reference_contact_number": "7200098"}])
        
        therapy = self.insertOne("therapy", {
            "title": "Test therapy",
            "area_id": "0",
            "time": "19:00:00",
            "date": "2023-03-27",
            "therapy_status": "open",
            "duration": 60
        })
        print("therapy id: ", therapy)

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
    
    def insertMany(self, collectionName, list):
        response = self.db[collectionName].insert_many(list)
        return response.inserted_ids

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
