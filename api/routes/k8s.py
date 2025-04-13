from flask import Blueprint, jsonify
import os, json

bp = Blueprint('k8s', __name__, url_prefix='/k8s')

@bp.route("/", methods=["GET"])
def get_data():
    path = os.path.join("output", "k8s.json")
    if os.path.exists(path):
        with open(path) as f:
            return jsonify(json.load(f))
    return jsonify({"error": "No data found"}), 404
