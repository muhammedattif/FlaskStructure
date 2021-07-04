
from flask_restful import Resource, Api
from flask import request
import json
class dashboard(Resource):
    def post(self):

        return {'name':request}
