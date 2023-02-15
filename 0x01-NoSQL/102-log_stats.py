#!/usr/bin/env python3
"""
Improve 12-log_stats.py by adding the top 10 of the most
present IPs in the collection nginx of the database logs
"""


def logs():
    """Python script that provides some stats about
    Nginx logs stored in MongoDB"""
    import pymongo
    # from pprint import pprint
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
    print("Methods:")
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

    # get most present IP address
    pipeline = [
            {
            "$group": {
                "_id": "$ip",
                "ip_count": {"$sum": 1}
                }
            },
            {"$sort": {"ip_count": -1 }},
            {"$limit": 10}
            ]
    ips = logs_collection.aggregate(pipeline)
    print("IPs:")
    for ip in ips:
        print("\t{}: {}".format(ip['_id'], ip['ip_count']))



if __name__ == "__main__":
    logs()
