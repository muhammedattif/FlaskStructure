from flask_restful import Resource, Api, reqparse
from flask import request, jsonify
import json
import requests
import os

class dashboard2(Resource):
    def get(self):
        return {'d':'d'}
