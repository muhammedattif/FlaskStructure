from flask_restful import Resource
from flask import request
import json
import requests
import os
import owncloud

from helpers.utils import *
import settings

class CallApi(Resource):


    def post(self):
        data = request.get_json()

        end_point = data['url']
        erp_url = settings.ERP_URL + end_point

        headers = {"Authorization": settings.ERP_TOKEN}

        response = requests.post(erp_url, data = json.dumps(data['data']), headers = headers)
        return response.json()


    def postt(self):
        image = request.files['file']
        image.save(os.path.join(image.filename))

        if not is_valid_image(image):
            os.remove(image.filename)
            return {'message': 'File must be less than 10MB'}
        try:
            oc = owncloud.Client(settings.CLOUD_URL)
            oc.login(settings.CLOUD_USERNAME, settings.CLOUD_PASSWORD)
            # oc.mkdir('upload/123')
            oc.put_file('upload/123/123.txt', image.filename)
            link_info = oc.share_file_with_link('upload/123/123.txt')
            os.remove(settings.BASE_DIR + str(image.filename))

            # we can also use
            #os.path.join(settings.BASE_DIR, str(image.filename))

        except Exception as e:
            return {'message': 'down'}

        return {'Here is your link:' :link_info.get_link() }

    def put(self):
        pass

    def get(self):

        end_point = request.args.get('url')
        erp_url = settings.ERP_URL + str(end_point)
        headers = {"Authorization":settings.ERP_TOKEN}

        # must wrapped by try, except clause
        try:
            response = requests.get(erp_url, headers = headers)

            return response.json()
        except:
            return {'message': 'something went wrong!'}, 5200

    def delete(self):
        pass
