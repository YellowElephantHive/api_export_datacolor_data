import os
import sys

import flask
from flask import Flask
from flask_restful import Resource, Api
import sqlite3

# TODO: set environment path

cwd = os.getcwd()
DatabasePath = os.path.join(cwd)
con = sqlite3.connect(database=)


app = Flask(__name__)
api = Api(app)
api.debug = True


class Working(Resource):
    def get(self):
        return 'This api is working.'

api.add_resource(Working, '/')


class DataColor(Resource):
    def get(self):
        pass

api.add_resource(DataColor, '/api/get/data_color')

if __name__ == '__main__':
    api.run()
