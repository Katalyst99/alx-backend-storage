#!/usr/bin/env python3
"""The module for listing all documents in python"""


def list_all(mongo_collection):
    """Function that lists all documents in a collection"""
    emptyList = []
    if mongo_collection is None:
        return emptyList
    return mongo_collection.find()
