"""

"""
from flask import jsonify, request
from flask_restful import Resource, reqparse
from main.middleware.authentication import token_required
from main.models.authenticate import Authentication


class AuthenticationEndpoints(Resource):
    """

    """

    def __init__(self):
        """

        """
        self.model = Authentication()

    def post(self):
        """

        """
        data = request.get_json(force=True)
        staff_id = data['body']['_id']
        staff_password = data['body']['staff_password']
        print('id: ', staff_id)
        login = self.model.login(staff_id, staff_password)
        if login is None:
            print("login: ", login)
            return jsonify({"error": "Invalid credentials"})
        response = jsonify({'token': login})
        return response
