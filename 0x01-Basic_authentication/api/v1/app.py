#!/usr/bin/env python3
"""
Route module for the API
"""
from os import getenv
from api.v1.views import app_views
from flask import Flask, jsonify, abort, request
from flask_cors import (CORS, cross_origin)
import os


app = Flask(__name__)
app.register_blueprint(app_views)
CORS(app, resources={r"/api/v1/*": {"origins": "*"}})
auth = None
auth_type = os.getenv('AUTH_TYPE')
from api.v1.auth.auth import Auth
auth = Auth


@app.errorhandler(404)
def not_found(error) -> str:
    """ Not found handler
    """
    return jsonify({"error": "Not found"}), 404


@app.errorhandler(401)
def unathorized(error) -> str:
    '''
    unauthorized response
    '''

    return jsonify({"error": "Unauthorized"}), 401


@app.errorhandler(403)
def forbidden(error) -> str:
    '''
    forbidden error
    '''
    return jsonify({"error": "Forbidden"}), 403


@app.before_request()
def before_req():
    if auth is None:
        pass
    for requests in request.path:
        if requests not in request.path:
            pass
        from api.v1.auth import require_auth
        if auth.authorization_header(request) == None:
            return abort(401)
        if auth.current_user(request) is None:
            return abort(403)



if __name__ == "__main__":
    host = getenv("API_HOST", "0.0.0.0")
    port = getenv("API_PORT", "5000")
    app.run(host=host, port=port)
