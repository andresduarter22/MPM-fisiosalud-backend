"""
File that contains all functions related with the shop article actions.
"""
from main.database_manager.db_manager import DbManager


class ShopArticle():
    """

    """

    def __init__(self):
        """

        """
        self.collection_name = "shopArticle"

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
        except:
            print("ay nooooo")
