#!/usr/bin/env python3
"""The module for having a specific topic"""


def schools_by_topic(mongo_collection, topic):
    """Function that returns the list of school having a specific topic"""
    if mongo_collection is None:
        return None
    return mongo_collection.find(
        {'topics': topic}
    )
