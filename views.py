from flask_restful import Resource, Api, reqparse
from flask import request, jsonify
import json
import requests
import os


class dashboard(Resource):

    def post(self):
        data = request.get_json()
        end_point = data['url']
        erp_url = os.getenv('BASE_URL') + end_point

        headers = {"Authorization":os.getenv('TOKEN')}

        response = requests.get(erp_url, headers = headers)
        return response.json()

    def put(self):
        pass

    def get(self):

        end_point = request.args.get('url')
        erp_url = os.getenv('BASE_URL') + end_point

        headers = {"Authorization":os.getenv('TOKEN')}

        response = requests.get(erp_url, headers = headers)
        return response.json()

    def delete(self):
        pass
