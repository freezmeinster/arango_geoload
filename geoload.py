#!/usr/bin/env python
import csv
import os
import sys
import argparse
from pyArango.connection import Connection

parser = argparse.ArgumentParser(description='Laod geo data')
parser.add_argument('--user',
                    action="store",
                    type=str,
                    default="root",
                    dest="user",
                    help="Username for arangodb server")
parser.add_argument('--passwd',
                    action="store",
                    type=str,
                    default="root",
                    dest="passwd",
                    help="Password for arangodb server")
parser.add_argument('--host',
                    action="store",
                    type=str,
                    default="http://127.0.0.1:8529",
                    dest="host",
                    help="Password for arangodb server")
parser.add_argument('--db',
                    action="store",
                    type=str,
                    dest="db",
                    required=True,
                    help="Database name")
parser.add_argument('--type',
                    action="store",
                    type=str,
                    dest="type",
                    required=True,
                    help="Collection name")
parser.add_argument('inputfile',
                    action="store",
                    type=str,
                    help="File name")
args = parser.parse_args()

def run_load():
    config = vars(args)
    data_type = config.get("type")
    coll_name = "Geo" + data_type.title()
    conn = Connection(arangoURL=config.get("host"),
                      username=config.get("user"),
                      password=config.get("passwd")
                      )
    if data_type == "province" :
        fieldnames = ['code', 'name']
    elif data_type == "city" :
        fieldnames = ["code", "code", "name"]
    else :
        fieldnames = ["code", "code", "name"]
    with open(config.get("inputfile"), "rb") as csvfile :
        reader = csv.DictReader(csvfile, fieldnames=fieldnames)
        for row in reader:
            print row
    

if __name__ == '__main__':
    run_load()