import requests
from flask import Flask, request, jsonify

app = Flask(__name__)

GEOCODING_URL = 'https://nominatim.openstreetmap.org/search'
WEATHER_URL = 'https://api.open-meteo.com/v1/forecast'

@app.route('/weather', methods=['GET'])
def get_weather():
    city = request.args.get('city')
    if not city:
        return jsonify({"error": "Veuillez spécifier une ville."}), 400

    # Obtenir les coordonnées géographiques de la ville
    geocoding_params = {
        'q': city,
        'format': 'json',
        'limit': 1
    }
    geocoding_response = requests.get(GEOCODING_URL, params=geocoding_params)
    if geocoding_response.status_code != 200 or not geocoding_response.json():
        return jsonify({"error": "Impossible de récupérer les coordonnées pour la ville spécifiée."}), 404

    geocoding_data = geocoding_response.json()[0]
    latitude = geocoding_data['lat']
    longitude = geocoding_data['lon']

    # Obtenir les données météo en utilisant Open-Meteo
    weather_params = {
        'latitude': latitude,
        'longitude': longitude,
        'current_weather': 'true'
    }
    weather_response = requests.get(WEATHER_URL, params=weather_params)
    if weather_response.status_code != 200:
        return jsonify({"error": "Impossible de récupérer les données météo pour la ville spécifiée."}), weather_response.status_code

    weather_data = weather_response.json()['current_weather']
    weather_info = {
        'city': city,
        'temperature': weather_data['temperature'],
        'wind_speed': weather_data['windspeed'],
        'description': weather_data['weathercode']  # Code météo, peut être interprété selon la doc Open-Meteo
    }

    return jsonify(weather_info)

if __name__ == '__main__':
    app.run(debug=True)
