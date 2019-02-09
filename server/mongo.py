import pymongo
from flask import jsonify
from bson.json_util import dumps

myclient = pymongo.MongoClient("mongodb://localhost:27017/")

mydb = myclient["veni"]
mycol = mydb["events"]

def addEvent(event):
    res = mycol.insert_one(event)
    # if res.inserted_id is not None:
    #     return jsonify('{ "success": "1" }')
    # else:
    #     return jsonify('{ "success": "0" }')


def getEvents():
    events = []
    for x in mycol.find({}):
        events.append(dumps(x))
    return jsonify(events)


def getEvent(id):
    event = mycol.find({ 'id': id })
    return jsonify(event)


def removeEvent(id):
    res = mycol.delete_one({ 'id': id })
    if res.deleted_count > 0:
        return jsonify('{ "success": 1 }')
    else:
        return jsonify('{ "success": 0 }')
