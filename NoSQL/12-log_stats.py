#!/usr/bin/env python3
'''Provides some stats stored in MongoDB'''


from pymongo import MongoClient


def log_stats():
    '''Provides some stats'''
    client = MongoClient('mongodb://127.0.0.1:27017')
    db = client.logs
    collection = db.nginx

    num_logs = collection.count_documents({})
    print(f"{num_logs} logs")

    print("Methods:")
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    for method in methods:
        value = collection.count_documents({"method": method})
        print(f"\tmethod {method}: {value}")

    status_log = collection.count_documents(
        {"method": "GET", "path": "/status"})
    print(f"{status_log} status check")


if __name__ == "__main__":
    log_stats()