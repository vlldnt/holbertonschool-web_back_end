#!/usr/bin/env python3
''' Changes all topic of a school document based the name'''


from pymongo import MongoClient


def update_topics(mongo_collection, name, topics):
    ''' Changes all topic of a school document based the name'''
    mongo_collection.update_many(
        {"name": name},
        {"$set": {"topics": topics}}
    )
