#!/usr/bin/env python3
'''SImple basic Flask app'''

from flask import Flask
from auth import Auth
from flask import jsonify, request, abort, redirect

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


@app.route("/sessions", methods=['POST'])
def login():
    '''Login method implemented'''
    email = request.form.get("email")
    pwd = request.form.get('password')
    valid_login = AUTH.valid_login(email, pwd)
    if valid_login:
        session_id = AUTH.create_session(email)
        response = jsonify({"email": email, "message": "logged in"})
        response.set_cookie('session_id', session_id)
        return response
    else:
        abort(401)


@app.route("/sessions", methods=['DELETE'])
def logout():
    """Method to logout"""
    session_id = request.cookies.get("session_id")
    if session_id is None:
        abort(403)

    user = AUTH.get_user_from_session_id(session_id)
    if user is None:
        abort(403)
    AUTH.destroy_session(user.id)
    return redirect("/")


@app.route("/profile", methods=['GET'])
def profile():
    """Get user profile"""
    session_id = request.cookies.get("session_id")
    if session_id is None:
        abort(403)

    user = AUTH.get_user_from_session_id(session_id)
    if user is None:
        abort(403)

    return jsonify({"email": user.email})


@app.route("/reset_password", methods=['POST'])
def get_reset_password_token():
    """Get reset password token"""
    email = request.form.get("email")

    try:
        reset_token = AUTH.get_reset_password_token(email)
        return jsonify({"email": email, "reset_token": reset_token})
    except ValueError:
        abort(403)


@app.route("/reset_password", methods=['PUT'])
def update_password():
    """Update password"""
    email = request.form.get("email")
    reset_token = request.form.get("reset_token")
    new_password = request.form.get("new_password")

    try:
        AUTH.update_password(reset_token, new_password)
        return jsonify({"email": email, "message": "Password updated"})
    except ValueError:
        abort(403)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5001")
