from pymongo import MongoClient
import csv
import re


class MongoDBImporter:
    def __init__(self, csv_file, delimiter, host, db_name, user, password):
        self.csv = csv_file
        self.delimiter = delimiter
        self.host = host
        self.db_name = db_name
        self.user = user
        self.password = password

    def import_csv(self):
        collection = self.connect()
        #read from csv and insert
        with open(self.csv, mode='r') as csv_file:
            csv_reader = csv.DictReader(csv_file, delimiter=self.delimiter)
            for row in csv_reader:
                record = {re.sub('[^0-9a-zA-Z]+', '_', key): value for key, value in row.items()}
                collection.insert(record)
        return

    def connect(self):
        credentials = ""
        if self.user:
            credentials = self.user + ":" + self.password + "@"
        client = MongoClient("mongodb://" + credentials + self.host + ":27017/")
        db = client[self.db_name]
        return db[self.get_collection()]

    def get_collection(self):
        return self.csv.replace(".csv", "")
