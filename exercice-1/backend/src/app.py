import os
from flask import Flask

app = Flask(__name__)

@app.route("/api/hello")
def messageToShow():
    return "Hello World"


if __name__ == "__main__":
    port = int(os.getenv("BACKEND_PORT"))
    app.run(host="0.0.0.0", port=port)