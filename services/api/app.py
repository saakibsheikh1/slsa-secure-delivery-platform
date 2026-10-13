
import os
from flask import Flask, jsonify

app = Flask(__name__)

APP_NAME = "secure-delivery-api"
APP_VERSION = os.getenv("APP_VERSION", "1.0.0")
APP_ENVIRONMENT = os.getenv("APP_ENVIRONMENT", "development")


@app.get("/")
def home():
    return jsonify({
        "application": APP_NAME,
        "version": APP_VERSION,
        "environment": APP_ENVIRONMENT,
        "message": "Secure delivery API is running"
    })


@app.get("/health")
def health():
    return jsonify({
        "status": "healthy"
    }), 200


@app.get("/version")
def version():
    return jsonify({
        "application": APP_NAME,
        "version": APP_VERSION
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
