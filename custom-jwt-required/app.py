from functools import wraps
from flask import Flask, abort

from flask_jwt_extended import create_access_token
from flask_jwt_extended import get_jwt
from flask_jwt_extended import JWTManager
from flask_jwt_extended import verify_jwt_in_request
from flask_jwt_extended import jwt_required

app = Flask(__name__)
jwt = JWTManager(app)
app.config['JWT_SECRET_KEY'] = 'XJ3vmK&5SQ}SS9WN?smA'


@jwt.expired_token_loader
def custom_expired_token_loader_callback(*args):
    return {
        "msg": "Ex"
    }, 419

# def refresh_required():
#     def wrapper(fn):
#         @wraps(fn)
#         def decorator(*args, **kwargs):
#             try:
#                 verify_jwt_in_request()
#             except Exception as e:
#                 print(e)
#
#         return decorator
#
#     return wrapper


@app.route('/token')
def token():
    return {
        "token": create_access_token(identity="email")
    }


@app.route('/')
@jwt_required()
def index():
    return {
        "ok": True
    }
