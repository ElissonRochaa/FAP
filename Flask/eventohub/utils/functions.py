from functools import wraps
from flask import request, jsonify
import jwt

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        auth_header = request.headers.get('Authorization')
        if not auth_header:
            return jsonify({"Error":"Token não enviado"}), 401
        auth_header = auth_header.replace("Bearer ", "")
        print(auth_header)
        if not validate_token(auth_header):
            return jsonify({"Error":"Authentication required"}), 401
        return f(*args, **kwargs)
    return decorated_function

def role_required(required_roles):
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            auth_header = request.headers.get('Authorization')
            if not auth_header:
                return jsonify({"Error":"Authentication required"}), 401
            
            auth_header = auth_header.replace("Bearer ", "")
            payload = validate_token(auth_header)
            if not payload:
                return jsonify({"Error":"Invalid token"}), 401

            user_role = payload.get('role')
            if user_role not in required_roles:
                return jsonify({"Error":"Permission denied"}), 403
            
            return f(*args, **kwargs)
        return decorated_function
    return decorator

def validate_token(token):
    try:
        payload = jwt.decode(token, "FAPeventohub", algorithms=["HS256"])
        return payload
    except jwt.ExpiredSignatureError:
        raise ValueError("Token has expired")
    except jwt.InvalidTokenError:
        raise ValueError("Invalid Token")

# def permission_role():
#     return None