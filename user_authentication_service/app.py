#!/usr/bin/env python3
'''SImple basic Flask app'''

from flask import Flask
from auth import Auth
from flask import jsonify, request

app = Flask(__name__)
AUTH = Auth()


@app.route("/", methods=['GET'])
def bienvenue():
    '''Home message'''
    return jsonify({'message': 'Bienvenue'})


@app.route("/users", methods=['POST'])
def post_user():
    '''Post a new user'''
    email = request.form.get("email")
    password = request.form.get('password')
    try:
        user = AUTH.register_user(email, password)
        return jsonify({"email": user.email, "message": "user created"})
    except ValueError:
        return jsonify({"message": "email already registered"}), 400


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5001")
