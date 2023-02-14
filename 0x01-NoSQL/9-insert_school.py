#!/usr/bin/env python3
"""
Write a Python function that inserts a new document
in a collection based on kwargs:

    Prototype: def insert_school(mongo_collection, **kwargs):
    mongo_collection will be the pymongo collection object
    Returns the new _id
"""


def insert_school(mongo_collection, **kwargs):
    """inserts a new document in a collection based on kwargs"""
    obj = dict()
    for key, val in kwargs.items():
        obj[key] = val
    inserted_obj = mongo_collection.insert_one(obj)
    return inserted_obj.inserted_id
