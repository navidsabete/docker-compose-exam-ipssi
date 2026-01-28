import os
from flask import Flask, jsonify, request
from db import get_connection, init_db
from model import User

app = Flask(__name__)

init_db()

@app.route("/api/users", methods=["GET"])
def get_users():
    users = User.get_all()
    return jsonify([{"id": u.id, "username": u.username, "password": "*******"} for u in users])

@app.route("/api/users/create", methods=["POST"])
def create_user():
    username = request.form.get("username")
    password = request.form.get("password")
    if not username or not password:
        return {"error": "Missing data"}, 400
    user = User.create(username, password)
    return {"id": user.id, "username": user.username}, 201

@app.route("/api/users/<int:user_id>", methods=["GET"])
def get_user(user_id):
    user = User.get_user_details(user_id)
    if user:
        return jsonify({"id": user.id, "username": user.username, "password": "*********"})
    return jsonify({"error": "User not found"}), 404

@app.route("/api/users/<int:user_id>", methods=["PUT"])
def update_user(user_id):
    username = request.form.get("username")
    password = request.form.get("password")
    user = User.get_user_details(user_id)
    if not user:
        return jsonify({"error": "User not found"}), 404
    user.update(username, password)
    return jsonify({"id": user.id, "username": user.username})


@app.route("/api/users/<int:user_id>", methods=["DELETE"])
def delete_user(user_id):
    user = User.get_user_details(user_id)
    if not user:
        return jsonify({"error": "User not found"}), 404
    user.delete()
    return jsonify({"message": "Deleted"}), 200


if __name__ == "__main__":
    port = int(os.getenv("BACKEND_PORT"))
    app.run(host="0.0.0.0", port=port)