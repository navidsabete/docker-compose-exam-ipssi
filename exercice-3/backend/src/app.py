import os
import requests
from flask import Flask, jsonify


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



if __name__ == "__main__":
    app.run(host="0.0.0.0", port=BACKEND_PORT)
    