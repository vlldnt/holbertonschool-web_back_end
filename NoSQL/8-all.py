#!/usr/bin/env python3
'''function that lists all documents in a collection'''


from pymongo import MongoClient


def list_all(mongo_collection):
    '''Return empty list if None r a list of all documents'''
    if mongo_collection is None:
        return []
    return list(mongo_collection.find())
