#!/usr/bin/env python3
""" MongoDB Operations with Python using pymongo """

def list_all(mongo_collection):
    documents = []
    try:
        cursor = mongo_collection.find({})
        for document in cursor:
            documents.append(document)
    except Exception as e:
        print(f"An error occurred: {e}")
    return documents
