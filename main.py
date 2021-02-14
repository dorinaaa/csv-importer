from flask import Flask
from flask_restful import Api, Resource, reqparse

from Importer import Importer

Importer().get()


#app = Flask(__name__)
#api = Api(app)

#api.add_resource(Importer, "/import-csv/<int:id>")

#if __name__ == '__main__':
 #   app.run(debug=True, threaded=true)
