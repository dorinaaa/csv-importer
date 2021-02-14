from importers.mysql.MySQLImporter import MySQLImporter
from importers.mongodb.MongoDBImporter import MongoDBImporter


destinations = ["mysql", "slq-server", "mongodb"]


class DestinationChooser:

    def import_to_destination(self, csv, delimiter, db, host, port, db_name, user, password, create_table):
        if db in destinations:
            if db == "mysql":
                return MySQLImporter(csv, delimiter, host, db_name, user, password, create_table).import_csv()
            elif db == "mongodb":
                return MongoDBImporter(csv, delimiter, host, db_name, user, password).import_csv()
