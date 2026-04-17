import os
from pathlib import Path

from flask import Flask, Response, jsonify, request
import requests


app = Flask(__name__)

API_BASE = os.getenv("PHARMACY_API_BASE", "http://127.0.0.1:8000/api")
HTML_FILE = Path(__file__).resolve().parent / "pharmacy_inventory.html"


def proxy_request(path):
    target_url = f"{API_BASE}/{path}"
    headers = {"Accept": "application/json"}
    if request.method in {"POST", "PUT"}:
        headers["Content-Type"] = "application/json"

    response = requests.request(
        method=request.method,
        url=target_url,
        json=request.get_json(silent=True),
        headers=headers,
        timeout=15,
    )
    return jsonify(response.json()), response.status_code


@app.route("/")
def index():
    return Response(HTML_FILE.read_text(encoding="utf-8"), mimetype="text/html")


@app.route("/api/medicines", methods=["GET", "POST"])
def medicines():
    try:
        return proxy_request("medicines")
    except Exception as error:
        return jsonify({"error": str(error)}), 500


@app.route("/api/medicines/<int:record_id>", methods=["GET", "PUT", "DELETE"])
def medicine_detail(record_id):
    try:
        return proxy_request(f"medicines/{record_id}")
    except Exception as error:
        return jsonify({"error": str(error)}), 500


if __name__ == "__main__":
    print("Starting Pharmacy Inventory Web App...")
    print("Open your browser to: http://127.0.0.1:5000")
    print(f"Proxying Laravel API at: {API_BASE}")
    app.run(debug=True, port=5000)
