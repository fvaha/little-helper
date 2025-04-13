from flask import Blueprint, jsonify
import os
import json

bp = Blueprint('sysinfo', __name__, url_prefix='/sysinfo')

@bp.route("/", methods=["GET"])
def get_data():
    filepath = os.path.join("output", "sysinfo.json")
    if os.path.exists(filepath):
        with open(filepath) as f:
            data = json.load(f)
        return jsonify(data)
    else:
        return jsonify({"error": "No data found"}), 404
