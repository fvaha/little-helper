from flask import Blueprint, jsonify
import os, json

bp = Blueprint('docker', __name__, url_prefix='/docker')

@bp.route("/", methods=["GET"])
def get_data():
    path = os.path.join("output", "docker.json")
    if os.path.exists(path):
        with open(path) as f:
            return jsonify(json.load(f))
    return jsonify({"error": "No data found"}), 404
