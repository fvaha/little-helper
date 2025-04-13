from flask import Blueprint, jsonify
import os, json

bp = Blueprint('sysinfo', __name__, url_prefix='/sysinfo')

@bp.route("/", methods=["GET"])
def get_data():
    path = os.path.join("output", "sysinfo.json")
    if os.path.exists(path):
        with open(path) as f:
            return jsonify(json.load(f))
    return jsonify({"error": "No data found"}), 404
