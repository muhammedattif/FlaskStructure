
from flask import Flask
from dotenv import load_dotenv
from apps.dashboard.urls import urls
from flask_restful import Api
from flask_cors import CORS
import os

def create_app(name):

    app = Flask(name)

    #set RESTFul API
    api = Api(app)

    # load .env variables
    load_dotenv('.env')

    #load urls of each app
    for url in urls:
        api.add_resource(url[0],url[1])

    #set configuration environment
    app.config.from_object('config.'+ str(os.getenv('ENV')))

    # set CORS origin and Allowed Hosts
    CORS(app, resources={r"/*": {"origins": ["http://localhost:3000/*"]}})

    return app

app = create_app(__name__)

if __name__ == '__main__':
    app.run()
