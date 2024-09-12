#!/usr/bin/env python3
'''
Flask app module
'''
from flask import Flask, jsonify, requests
from auth import Auth


app = Flask(__name__)
app.config["JSONIFY_PRETTYPRINT_REGULAR"] = True
AUTH = Auth()

@app.route('/', methods=['GET'], strict_slashes=False)
def home('/'):
    '''
    Home route with a single get method
    Returns: jsonify response

    '''
    return jsonify({"message": "Bienvenue"})

@app.route('/users', methods=['POST'], strict_slashes=False)
def users():
    '''Endpoints to register users
        Args
            - email
            - password
    '''
    email = request.form.get("email")
    password = request.form.get("password")
    try:
        AUTH.register_user(email, password)
        return jsonify({"email": email, "message": "user created"})
    except ValueError:
        return jsonify({"message": "email already registered"}), 400


