#!/usr/bin/env python3
'''Return  a list of schools having a specific topic'''


from pymongo import MongoClient


def schools_by_topic(mongo_collection, topic):
    '''Return  a list of schools having a specific topic'''
    return list(mongo_collection.find({"topics": topic}))
