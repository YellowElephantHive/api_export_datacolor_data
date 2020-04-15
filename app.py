import os
import sys

import flask
from flask import Flask
from flask_restful import Resource, Api
import sqlite3

# TODO: set environment path
cwd = os.getcwd()
con = sqlite3.connect(database=)


app = Flask(__name__)
api = Api(app)
api.debug = True


class Working(Resource):
    def get(self):
        return 'This api is working.'

api.add_resource(Working, '/')

@api.route('/api/get/data_color')
class DataColor(Resource):
    def get(self):
        pass
        

if __name__ == '__main__':
    api.run()
