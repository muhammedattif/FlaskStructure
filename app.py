
from flask import Flask
from dotenv import load_dotenv
from urls import load_urls
from flask_restful import Api
from flask_cors import CORS
import os

def create_app(name):

    app = Flask(name)

    #set RESTFul API
    api = Api(app)

    # load apps urls
    api = load_urls(api)

    # load .env variables
    load_dotenv('.env')

    #set configuration environment
    app.config.from_object('config.'+ str(os.getenv('ENV')))

    # set CORS origin and Allowed Hosts
    CORS(app, resources={r"/*": {"origins": ["http://localhost:3000/*"]}})

    return app

app = create_app(__name__)

if __name__ == '__main__':
    app.run()
