# app_server.py

import os
import sys

from flask import Flask
from flask_restplus import Resource, Api

# Import Resources
from apis.module_name import api as module


app = Flask(__name__)

api = Api(  app,
            version='1.0',
            title='Service Name - API docs',
            description=''
)
app.config.SWAGGER_UI_JSONEDITOR = True


# Endpoint Service
api.add_namespace(module, path='/v1/end_point')


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
