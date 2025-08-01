from flask import Blueprint, request, jsonify
from weatherservice.weather import load_weather_data

weather_bp = Blueprint('api', __name__)

@weather_bp.route('/data', methods=['POST'])
def handle_data():
    data = request.json
    if not data or 'city' not in data:
        return jsonify({"error": "City not provided"}), 400

    city = data['city']['label']
    data = load_weather_data(city)
    
    
    return jsonify({"weather_data": data}), 200


