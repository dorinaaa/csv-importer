import pymysql
import csv
import pandas as pd
import re


class SQLServerImporter:
    def __init__(self, csv_file, delimiter, host, db_name, user, password, create_table):
        self.csv = csv_file
        self.delimiter = delimiter
        self.host = host
        self.db_name = db_name
        self.user = user
        self.password = password
        self.create_table = create_table

    def import_csv(self):
        cursor = self.connect()
        table_name = self.get_table(cursor)
        #read from csv and insert
        with open(self.csv, mode='r') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=self.delimiter)
            line_count = 0
            for row in csv_reader:
                #ignore columns row
                if line_count == 0:
                    line_count += 1
                    continue
                else:
                    print(row)
                    self.insert(cursor, table_name, row)
                    line_count += 1
        return

    def connect(self):
        return pymysql.connect(self.host, self.user, self.password, self.db_name, autocommit=True).cursor()

    def get_table(self, cursor):
        table_name = self.csv.replace(".csv", "")
        if self.create_table:
            self.create_db_table(cursor, table_name)
        return table_name

    def create_db_table(self, cursor, table_name):
        columns = self.get_columns()
        columns_text = "( "
        for column in columns:
            columns_text = columns_text + re.sub('[^0-9a-zA-Z]+', '_', column) + " varchar(" + str(self.get_column_length(columns, column)) + "),"
        cursor.execute("create table " + table_name + columns_text.rstrip(",") + ")")

    def get_columns(self):
        with open(self.csv, mode='r') as csv_file:
            csv_reader = csv.reader(csv_file)
            line_count = 0
            for row in csv_reader:
                if line_count == 0:
                    return row

    def get_column_length(self, columns, column_name):
        df = pd.read_csv(self.csv, names=columns)
        column_items = df[column_name].to_list()
        longest_item = max(column_items, key=len)
        return len(longest_item)

    def insert(self, cursor, table_name, record):
        record_values = ["\"" + r + "\"" for r in record]
        cursor.execute("insert ignore into " + table_name + " values (" + ",".join(record_values) + ")")






