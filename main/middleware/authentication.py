from functools import wraps
from secrets import token_urlsafe
from flask import jsonify, request, abort


def token_required(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        token = None
        if "Authorization" in request.headers:
            token = request.headers["Authorization"].split(" ")[1]
        
        if not token:
            return {"error": "Token is missing"}, 403
        
        if token != "test_jwt_token":
            return {"error": "Invalid token"}, 401

        return f(*args, **kwargs)
    return wrapper
