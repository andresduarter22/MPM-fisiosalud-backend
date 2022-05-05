"""

"""
from main.database_manager.db_manager import DbManager
from config import (
    JWT_ALGORITHM,
    JWT_ISSUER,
    JWT_PRIVATE_KEY,
    JWT_AUTH_DURATION,
    JWT_REFRESH_DURATION,
)
import hashlib
import jwt
from calendar import timegm
from datetime import datetime, timezone
from main.utils.constants import TokenType


class Authentication:
    """ """

    def __init__(self):
        """ """
        pass

    def authenticate(self, id, password_hash):
        """ """
        filter = {"_id": id}
        staff = {}
        try:
            staff = DbManager.get_instance().select("staff", filter)
        except:
            print("ay nooooo")
        hasher = hashlib.sha256()
        hasher.update(password_hash.encode("utf-8"))
        if len(staff) != 1:
            return None

        if staff[0]["staff_password"] == hasher.hexdigest():
            return self.generate_token(staff[0]["_id"])
        else:
            return None

    def generate_token(self, staff_id):
        iat = timegm(datetime.now(tz=timezone.utc).utctimetuple())
        exp = iat + JWT_AUTH_DURATION
        access_token = jwt.encode(
            {
                "iss": JWT_ISSUER,
                "iat": iat,
                "exp": exp,
                "staff_id": staff_id,
                "type": TokenType.ACCESS,
            },
            JWT_PRIVATE_KEY,
            algorithm=JWT_ALGORITHM,
        )
        exp = iat + JWT_REFRESH_DURATION
        refresh_token = jwt.encode(
            {
                "iss": JWT_ISSUER,
                "iat": iat,
                "exp": exp,
                "staff_id": staff_id,
                "type": TokenType.REFRESH,
            },
            JWT_PRIVATE_KEY,
            algorithm=JWT_ALGORITHM,
        )

        return access_token, refresh_token
