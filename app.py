from flask import Flask
from flask_cors import CORS
from routes.v1.weatherdata import weather_bp
from routes.v1.alldata import all_data_bp

app = Flask(__name__)
CORS(app)

app.register_blueprint(weather_bp, url_prefix='/api')
app.register_blueprint(all_data_bp, url_prefix='/data')


if __name__ == '__main__':
    app.run(host='localhost', port=5000)
