"""

"""
from main.database_manager.db_manager import DbManager
import hashlib


class Authentication():
    """
    
    """

    def __init__(self):
        """
        
        """
        pass

    def login(self, id, password_hash):
        """
        
        """
        filter = {
            "_id": id
        }
        try:
            staff = DbManager.get_instance().select("staff", filter)
        except:
            print("ay nooooo")
        print("staff: ", staff)
        hasher = hashlib.sha256()
        hasher.update(password_hash.encode('utf-8'))
        if len(staff) == 0:
            return None

        if staff[0]['staff_password'] == hasher.hexdigest():
            return "test_jwt_token"
        else:
            return None