from flask_restful import Api, Resource, reqparse

from DestinationChooser import DestinationChooser


class Importer(Resource):

    def get(self):
        #parser = reqparse.RequestParser()
        #params = parser.parse_args()
        #csv_file = params["csv"]
        #delimiter = params["delimiter"]
        #db = params["db"]
        #host = params["host"]
        #port = params["port"]
        #db_name = params["db_name"]
        #user = params["user"]
        #password = params["password"]
        #create_table = params["create_table"]
        csv_file = "test.csv"
        delimiter = ","
        db = "mysql"
        db = "mongodb"
        host = "127.0.0.1"
        port = "2707"
        db_name = "test"
        user = ""
        password = ""
        create_table = 0
        destination_chooser = DestinationChooser()
        destination_chooser.import_to_destination(csv_file, delimiter, db, host, port,db_name, user, password, create_table)


