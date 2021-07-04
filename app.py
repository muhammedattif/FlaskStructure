from flask import Flask
from apps.dashboard.urls import urls
from flask_restful import Api


def create_app(name):
    app = Flask(name)
    api = Api(app)

    for url in urls:
        api.add_resource(url[0],url[1])
    return app

app = create_app(__name__)

if __name__ == '__main__':
    app.run(debug=True)
