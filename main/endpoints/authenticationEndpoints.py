"""

"""
from flask import request
from flask_restful import Resource
from main.models.authenticate import Authentication
from main.middleware.authentication import refresh_token


class AuthenticationEndpoints(Resource):
    """ """

    def __init__(self):
        """ """
        self.model = Authentication()

    def post(self):
        """ """
        data = request.get_json(force=True)
        if data is None or data == {}:
            return {}, 400
        staff_id = data["_id"]
        staff_password = data["password"]
        tokens = self.model.authenticate(staff_id, staff_password)

        if tokens is None:
            return {"error": "Authentication error"}, 403
        else:
            access_token, refresh_token = tokens

        return {
            "access_token": access_token,
            "refresh_token": refresh_token,
        }

    @refresh_token
    def put(self, **kwargs):
        tokens = self.model.generate_token(kwargs["staff_id"])

        if tokens is None:
            return {"error": "Invalid credentials"}, 403
        else:
            access_token, refresh_token = tokens

        return {
            "access_token": access_token,
            "refresh_token": refresh_token,
        }
