#!/usr/bin/env python3
'''SImple basic Flask app'''

from flask import Flask
from auth import Auth
from flask import jsonify

app = Flask(__name__)
AUTH = Auth()


@app.route("/", methods=['GET'])
def bienvenue():
    return jsonify({'message': 'Bienvenue'})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5001")
