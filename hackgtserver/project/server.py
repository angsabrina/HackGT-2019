from flask import Flask, request, json
from . import util, database as db

import asyncio

api = Flask(__name__)

@api.route('/user/create', methods=['POST'])
def create_username():
    username = request.args.get('username', type = str)
    password = request.args.get('password', type = str)
    hashed = util.generate_first_hashed(password)
    success = db.create_user(username, password)
    if success:
        return json.dumps({"success": True}), 201
    else:
        return json.dumps({"success": False}), 500

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

if __name__ == '__main__':
    api.run()