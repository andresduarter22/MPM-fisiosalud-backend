import jwt
from functools import wraps
from flask import request
from config import JWT_ISSUER, JWT_PRIVATE_KEY, JWT_ALGORITHM
from jwt import InvalidIssuedAtError, ExpiredSignatureError, InvalidIssuerError

from main.utils.constants import TokenType


def token_required(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        token = None
        if "Authorization" in request.headers:
            token = request.headers["Authorization"].split(" ")[1]

        if not token:
            return {"error": "Token is missing"}, 403

        try:
            decoded_payload = jwt.decode(
                token, JWT_PRIVATE_KEY, algorithms=[JWT_ALGORITHM], issuer=JWT_ISSUER
            )
            if not decoded_payload["type"] == TokenType.ACCESS:
                return {"error": "Not an access_token"}, 401
        except InvalidIssuedAtError as e:
            print(e)
            return {"error": str(e)}, 401
        except ExpiredSignatureError as e:
            print(e)
            return {"error": str(e)}, 401
        except InvalidIssuerError as e:
            print(e)
            return {"error": str(e)}, 401
        except:
            return {"error": "Invalid token"}, 401
        else:
            return f(*args, **kwargs)

    return wrapper


def refresh_token(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        token = None
        if "Authorization" in request.headers:
            token = request.headers["Authorization"].split(" ")[1]

        if not token:
            return {"error": "Token is missing"}, 403

        try:
            decoded_payload = jwt.decode(
                token, JWT_PRIVATE_KEY, algorithms=[JWT_ALGORITHM], issuer=JWT_ISSUER
            )
            kwargs["staff_id"] = decoded_payload["staff_id"]
            if not decoded_payload["type"] == TokenType.REFRESH:
                return {"error": "Not a refresh_token"}, 401
        except InvalidIssuedAtError as e:
            print(e)
            return {"error": str(e)}, 401
        except ExpiredSignatureError as e:
            print(e)
            return {"error": str(e)}, 401
        except InvalidIssuerError as e:
            print(e)
            return {"error": str(e)}, 401
        except:
            return {"error": "Invalid token"}, 401
        else:
            return f(*args, **kwargs)

    return wrapper
