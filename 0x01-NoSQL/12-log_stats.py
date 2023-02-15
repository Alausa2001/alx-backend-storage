#!/usr/bin/env python3
"""
Python script that provides some stats about Nginx logs stored in MongoDB:

    Database: logs
    Collection: nginx
    Display (same as the example):
    first line: x logs where x is the number of documents in this collection
    second line: Methods:
    5 lines with the number of documents with the method =
    ["GET", "POST", "PUT", "PATCH", "DELETE"] in this order
    (see example below - warning: it’s a tabulation before each line)
    one line with the number of documents with:
    method=GET
    path=/status
"""


def logs():
    """Python script that provides some stats about
    Nginx logs stored in MongoDB"""
    import pymongo
    client = pymongo.MongoClient('mongodb://127.0.0.1:27017')
    logs_collection = client.logs.nginx
    get = []
    post = 0
    put = 0
    patch = 0
    delete = 0
    count_all = 0
    for doc in logs_collection.find():
        count_all += 1
        if doc.get('method') == "GET":
            get.append(doc)
        elif doc.get('method') == "POST":
            post += 1
        elif doc.get('method') == "PUT":
            put += 1
        elif doc.get('method') == "PATCH":
            patch += 1
        elif doc.get('method') == "DELETE":
            delete += 1
    print("{} logs".format(count_all))
    print("methods:")
    print("\tmethod GET: {}".format(len(get)))
    print("\tmethod POST: {}".format(post))
    print("\tmethod PUT: {}".format(put))
    print("\tmethod PATCH: {}".format(patch))
    print("\tmethod DELETE: {}".format(delete))
    status_check = 0
    for get_method in get:
        if get_method.get('path') == '/status':
            status_check += 1
    print("{} status check".format(status_check))


if __name__ == "__main__":
    logs()
