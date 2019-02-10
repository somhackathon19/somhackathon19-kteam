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

def getEvent2(id):
    return mycol.find_one({"_id": ObjectId(id)})

def addUser(id, name):
    res = mycol.update({"_id": ObjectId(id)}, {'$push': {'participants': name}})

def removeUser(id, name):
    print(name)
    res = mycol.update({"_id": ObjectId(id)}, {'$pull': {'participants': name}})

def removeEvent(id):
    res = mycol.delete_one({ 'id': id })
