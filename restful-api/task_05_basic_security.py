#!/usr/bin/env python3

from flask import Flask, request, jsonify, make_response
from werkzeug.security import generate_password_hash, check_password_hash
from flask_httpauth import HTTPBasicAuth
from flask_jwt_extended import (
    JWTManager, create_access_token, jwt_required,
    get_jwt_identity, get_jwt
)

app = Flask(__name__)

app.config["JWT_SECRET_KEY"] = "abcd"
jwt = JWTManager(app)

auth = HTTPBasicAuth()

users = {
    "user1": {
        "username": "user1",
        "password": generate_password_hash("password"),
        "role": "user"
    },
    "admin1": {
        "username": "admin1",
        "password": generate_password_hash("password"),
        "role": "admin"
    }
}

@auth.verify_password
def verify_password(username, password):
    if not username or not password:
        return False
    user = users.get(username)
    if not user:
        return False
    return check_password_hash(user["password"], password)

@auth.error_handler
def basic_auth_error():
    return make_response(jsonify({"error": "Unauthorized"}), 401)

@app.get("/basic-protected")
@auth.login_required
def basic_protected():
    return "Basic Auth: Access Granted", 200

@app.post("/login")
def login():
    data = request.get_json(silent=True) or {}
    username = data.get("username")
    password = data.get("password")

    if not username or not password:
        return jsonify({"error": "Invalid credentials"}), 401

    user = users.get(username)
    if not user or not check_password_hash(user["password"], password):
        return jsonify({"error": "Invalid credentials"}), 401

    additional_claims = {"role": user["role"]}
    access_token = create_access_token(identity=username, additional_claims=additional_claims)
    return jsonify(access_token=access_token), 200

@app.get("/jwt-protected")
@jwt_required()
def jwt_protected():
    return "JWT Auth: Access Granted", 200

@app.get("/admin-only")
@jwt_required()
def admin_only():
    jwt_claims = get_jwt()
    role = jwt_claims.get("role")
    if not role:
        identity = get_jwt_identity()
        user = users.get(identity)
        role = user["role"] if user else None

    if role != "admin":
        return jsonify({"error": "Admin access required"}), 403

    return "Admin Access: Granted", 200

@jwt.unauthorized_loader
def handle_unauthorized(err_str):
    return jsonify({"error": "Missing or invalid token"}), 401

@jwt.invalid_token_loader
def handle_invalid_token(err_str):
    return jsonify({"error": "Invalid token"}), 401

@jwt.expired_token_loader
def handle_expired_token(*args, **kwargs):
    return jsonify({"error": "Token has expired"}), 401

@jwt.revoked_token_loader
def handle_revoked_token(*args, **kwargs):
    return jsonify({"error": "Token has been revoked"}), 401

@jwt.needs_fresh_token_loader
def handle_needs_fresh_token(*args, **kwargs):
    return jsonify({"error": "Fresh token required"}), 401

@app.errorhandler(400)
def bad_request(e):
    return jsonify({"error": "Bad request"}), 400

if __name__ == "__main__":
    app.run(debug=False)
