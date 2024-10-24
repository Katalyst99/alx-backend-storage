#!/usr/bin/env python3
"""The module for changing school topics"""


def update_topics(mongo_collection, name, topics):
    """
    Function that changes all topics of a school document based on the name
    """
    if mongo_collection is None:
        return None
    mongo_collection.update_many(
        {'name': name},
        {"$set": {'topics': topics}}
    )
