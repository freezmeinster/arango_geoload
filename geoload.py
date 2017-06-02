#!/usr/bin/env python
import csv
import os
import sys
import argparse
import multiprocessing as mp
from itertools import islice
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
                    choices=('province', 'city', 'district', 'village'),
                    help="Data type.")
parser.add_argument('inputfile',
                    action="store",
                    type=str,
                    help="File name")
args = parser.parse_args()

def worker(data, collection):
    for item in data:
        doc = collection.createDocument()
        for attr in item.keys():
            doc[attr] = item[attr]
        doc.save()
        print item
    return True

def data_spliter(data, slice_num):
    data = list(data)
    data_length = len(data)
    chunk_size = data_length / slice_num
    for i in range(0, data_length, chunk_size):
        # Create an index range for l of n items:
        yield data[i:i+chunk_size]

def run_load():
    config = vars(args)
    data_type = config.get("type")
    coll_name = "Geo" + data_type.title()
    conn = Connection(arangoURL=config.get("host"),
                      username=config.get("user"),
                      password=config.get("passwd")
                      )
    worker_count = mp.cpu_count() - 1
    db_name = config.get("db")
    if conn.hasDatabase(db_name):
        db = conn[db_name]
        
        if db.hasCollection(coll_name):
            collection = db[coll_name]
            collection.empty()
        else :
            collection = db.createCollection(name=coll_name)
            
        if data_type == "province" :
            fieldnames = ['code', 'name']
        elif data_type == "city" :
            fieldnames = ["code", "province", "name"]
        elif data_type == "district" :
            fieldnames = ["code", "city", "name"]
        elif data_type == "village" :
            fieldnames = ["code", "district", "name"]
            
        with open(config.get("inputfile"), "rb") as csvfile :
            reader = csv.DictReader(csvfile, fieldnames=fieldnames)
            jobs = []
            for row in data_spliter(reader, worker_count) :
                p = mp.Process(target=worker, args=[row,collection])
                jobs.append(p)
                p.start()
    else :
        print "Database %s not found " % db_name

if __name__ == '__main__':
    run_load()