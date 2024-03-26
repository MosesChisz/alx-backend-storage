#!/usr/bin/env python3

from pymongo import MongoClient

def nginx_logs_stats():
    # Connect to MongoDB
    client = MongoClient('mongodb://localhost://127.0.0.1:27017')
    db = client['logs']
    collection = db['nginx']

    # Total number of documents
    total_logs = collection.count_documents({})

    # Methods
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    method_counts = {method: collection.count_documents({"method": method}) for method in methods}

    # Number of documents with method=GET and path=/status
    status_count = collection.count_documents({"method": "GET", "path": "/status"})

    # Top 10 most present IPs
    top_ips = collection.aggregate([
        {"$group": {"_id": "$ip", "count": {"$sum": 1}}},
        {"$sort": {"count": -1}},
        {"$limit": 10}
    ])

    # Display stats
    print(f"{total_logs} logs where {total_logs} is the number of documents in this collection")
    print("Methods:")
    for method in methods:
        print(f"\t{method}: {method_counts[method]}")
    print(f"\tGET /status: {status_count}")
    print("Top 10 IPs:")
    for index, ip in enumerate(top_ips):
        print(f"\t{index+1}. {ip['_id']}: {ip['count']}")

if __name__ == "__main__":
    nginx_logs_stats()
