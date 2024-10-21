#!/usr/bin/env python3
"""The module for retrieving stats from Nginx logs"""
from pymongo import MongoClient


def Nginx_stats_logs(mongo_collection):
    """Retrieves the stats from Nginx logs stored in MongoDB"""
    numLogs = mongo_collection.count_documents({})
    print("{} logs".format(numLogs))

    print('Methods:')
    for method in ['GET', 'POST', 'PUT', 'PATCH', 'DELETE']:
        reqCount = mongo_collection.count_documents({'method': method})
        print(f"\tmethod {method}: {reqCount}")

    status = mongo_collection.count_documents(
            {'method': 'GET', 'path': '/status'})
    print('{} status check'.format(status))


if __name__ == "__main__":
    client = MongoClient('mongodb://127.0.0.1:27017')
    mongo_collection = client.logs.nginx
    Nginx_stats_logs(mongo_collection)
