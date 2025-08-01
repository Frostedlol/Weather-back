from flask import Blueprint, request, jsonify
from weatherservice.allweather import load_all_weather_data

all_data_bp = Blueprint('data', __name__)

@all_data_bp.route('/countrydata', methods=['POST'])
def handle_countrydata():
    data = request.json['cities']
    if not data:
        return jsonify({"error": "No cities provided"}), 400
    
    city_values = load_all_weather_data(data)
    return jsonify({"weather_data": city_values}), 200


