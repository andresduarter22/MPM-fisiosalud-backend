from bson.objectid import ObjectId
from main.utils.constants import COLLECTONS_WITHOUT_OBJECT_ID

def format_string(string):
    formated_string = string.replace(" ", "_")
    formated_string = formated_string.lower()
    return formated_string

def cleanBody(body):
    unset = {key: value for key, value in body.items() if value == ""}
    return body, unset

def addObjectId(filter, collection_name):
    if collection_name not in COLLECTONS_WITHOUT_OBJECT_ID:
        filter["_id"] = ObjectId(filter["_id"])
    return filter