from flask import Flask, request, json
from . import util, database as db

app = Flask(__name__)

@api.route('/users/create', methods=['POST'])
def create_username():
    username = request.args.get('username', type = str)
    password = request.args.get('password', type = str)
    hashed = util.generate_first_hashed(password)
    success = db.create_user(username, password)
    if success:
        return json.dumps({"success": True}), 201
    else:
        return json.dumps({"success": False}), 500

if __name__ == '__main__':
    app.run()