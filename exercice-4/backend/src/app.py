import os
import requests
from flask import Flask, jsonify, request
from db import SessionLocal, User


BACKEND_PORT = int(os.getenv("BACKEND_PORT"))

EXTERNAL_API_URL = os.getenv("EXTERNAL_API_URL")

TOR_PROXY_HOST = os.getenv("TOR_PROXY_HOST")
TOR_PROXY_PORT = os.getenv("TOR_PROXY_PORT")

FRONTEND_URL = os.getenv("FRONTEND_URL")
FRONTEND_PORT = os.getenv("FRONTEND_PORT")

nb_users_to_fetch = os.getenv("NB_RESULTS")

# Proxy SOCKS5 (DNS via Tor grâce à socks5h)
PROXIES = {
    "http": f"socks5h://{TOR_PROXY_HOST}:{TOR_PROXY_PORT}",
    "https": f"socks5h://{TOR_PROXY_HOST}:{TOR_PROXY_PORT}"
}

app = Flask(__name__)

@app.route("/tor-api/random-users", methods=["GET"])
def get_random_user():
    try:
        response = requests.get(
            f"{EXTERNAL_API_URL}/?results={nb_users_to_fetch}",
            proxies=PROXIES,
            timeout=10
        )
        response.raise_for_status()
    except requests.RequestException as e:
        return jsonify({"error": str(e)}), 500
    
    data = response.json()
    data_results = data.get("results")
    users = []
    for user in data_results:
        users.append({
            "name": f"{user['name']['title']} {user['name']['first']} {user['name']['last']}",
            "picture": user["picture"]["large"]
        })
    return jsonify(users)


@app.route("/api/users", methods=["GET"])
def get_users():
    db = SessionLocal()
    users = db.query(User).all()
    return jsonify([{"id": u.id, "username": u.username, "password": "*******"} for u in users])

@app.route("/api/users/create", methods=["POST"])
def create_user():
#    data = request.json
    username_data = request.form.get("username")
    password_data = request.form.get("password")
    db = SessionLocal()
    user = User(username=username_data, password=password_data)
    db.add(user)
    db.commit()
    return {"id": user.id, "username": user.username}, 201

@app.route("/api/users/<int:user_id>", methods=["GET"])
def get_user(user_id):
    db = SessionLocal()
    user = db.query(User).get(user_id)
    if user:
        return jsonify({"id": user.id, "username": user.username, "password": "*********"})
    return jsonify({"error": "User not found"}), 404

@app.route("/api/users/<int:user_id>", methods=["PUT"])
def update_user(user_id):
#    data = request.json
    username_data = request.form.get("username")
    password_data = request.form.get("password")
    db = SessionLocal()
    user = db.query(User).get(user_id)
    if not user:
        return jsonify({"error": "User not found"}), 404
    user.username = username_data
    user.password = password_data
    db.commit()
    return jsonify({"id": user.id, "username": user.username})


@app.route("/api/users/<int:user_id>", methods=["DELETE"])
def delete_user(user_id):
    db = SessionLocal()
    user = db.query(User).get(user_id)
    if not user:
        return jsonify({"error": "User not found"}), 404
    db.delete(user)
    db.commit()
    return jsonify({"message": "Deleted"}), 200




if __name__ == "__main__":
    app.run(host="0.0.0.0", port=BACKEND_PORT)
    