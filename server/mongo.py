import pymongo
from flask import jsonify
from bson.json_util import dumps
from bson.objectid import ObjectId

myclient = pymongo.MongoClient("mongodb://localhost:27017/")

mydb = myclient["veni"]
mycol = mydb["events"]

def addEvent(event):
    res = mycol.insert_one(event)

def getEvents():
    return dumps(mycol.find({}))

def getEvent(id):
    return dumps(mycol.find({"_id": ObjectId(id)}))

def removeEvent(id):
    res = mycol.delete_one({ 'id': id })
