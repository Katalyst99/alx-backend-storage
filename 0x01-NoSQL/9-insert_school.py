#!/usr/bin/env python3
"""The module for inserting a document in python"""


def insert_school(mongo_collection, **kwargs):
    """Function that inserts a new document in a collection based on kwargs"""
    if mongo_collection is None:
        return None
    newDoc = mongo_collection.insert_one(kwargs)
    return newDoc.inserted_id
