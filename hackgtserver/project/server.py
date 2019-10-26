from flask import Flask, request, json, make_response, jsonify
from . import util, database as db

import asyncio

api = Flask(__name__)

@api.route('/user/create', methods=['GET'])
def create_username():
    username = request.args.get('username', type = str)
    password = request.args.get('password', type = str)
    hashed = util.generate_first_hashed(password)
    success = db.create_user(username, password)
    if success:
        token = util.encode_auth_token(username)
        responseObject = {
            'success': True,
            'token': token.decode()
        }
        return make_response(jsonify(responseObject)), 201
    else:
        return json.dumps({"success": False}), 500
  
@api.route('/user/login', methods=['GET'])  
def log_user_in():
    username = request.args.get('username', type = str)
    password = request.args.get('password', type = str)
    hashed = db.get_user_password(username)
    success = util.check_password(password, hashed)
    if success:
        token = util.encode_auth_token(username)
        responseObject = {
            'success': True,
            'token': token.decode()
        }
        return make_response(jsonify(responseObject)), 200
    else:
        return json.dumps({"success": False}), 401

@api.route('/user/exist', methods=['POST'])
def is_username_exists():
    username = request.args.get('username', type = str)
    success = db.is_user_exists(username)
    if success:
        return json.dumps({"success": True}), 200
    elif success is None:
        return json.dumps({"success": False}), 500
    else:
        return json.dumps({"success": False}), 200
        
@api.route('/img/upload', methods=['POST'])
def upload_image():
    auth_header = request.headers.get('Authorization')
    if auth_header:
        auth_token = auth_header.split(" ")[1]
    else:
        auth_token = ''
    if auth_token:
        resp = util.decode_auth_token(auth_token)
        if not isinstance(resp, str):
            user = User.query.filter_by(id=resp).first()
            responseObject = {
                'success': True
            }
            return make_response(jsonify(responseObject)), 200
        responseObject = {
            'success': False,
            'message': resp
        }
        return make_response(jsonify(responseObject)), 401
    else:
        responseObject = {
                'success': False,
                'message': 'Provide a valid auth token.'
            }
        return make_response(jsonify(responseObject)), 401

if __name__ == '__main__':
    api.run()