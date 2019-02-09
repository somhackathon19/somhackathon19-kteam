import pymongo
from flask import jsonify
from bson.json_util import dumps

myclient = pymongo.MongoClient("mongodb://localhost:27017/")

mydb = myclient["veni"]
mycol = mydb["events"]

def addEvent(event):
    event = { "name": "John", "address": "Highway 37" }
    x = mycol.insert_one(event)
    return ''

def getEvents():
    # events = [
    #     {
    #         "id": 1,
    #         "titol": "bon dia",
    #         "descripcio": "hola bon dia"
    #     }
    # ]
    events = []
    for x in mycol.find({ 'id': 2 }):
        events.append(dumps(x))
    return jsonify(events)


def getEvent(id):
    event = mycol.find({ 'id': id }):
    return jsonify(events)
