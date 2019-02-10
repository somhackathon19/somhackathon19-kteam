from flask import Flask, request, jsonify
from mongo import *
from flask_socketio import SocketIO, send, emit
from flask_cors import CORS
from pdfcompleter import *

app = Flask(__name__)
app.config['SECRET_KEY'] = 'holabondiasomhackathon'
cors = CORS(app, resources={r"/*":{"origins":"*:*"}})
socketio = SocketIO(app)
socketio.run(app)

@socketio.on('getEvents')
def apiGetEvents():
    print('get events')
    emit('sendEvents', { 'data': getEvents() })

@socketio.on('getEvent')
def apiGetEvent(event):
    print('get event: ' + str(event['id']))
    emit('sendEvent', { 'data': getEvent(str(event['id'])) })

@socketio.on('addEvent')
def apiAddEvent(event):
    print('new event: ' + str(event))
    addEvent(event)
    emit('sendEvents', { 'data': getEvents() }, broadcast=True, namespace='/')

@socketio.on('unirse')
def apiAddEvent(event):
    print('unirse: ' + str(event))
    addUser(event['id'], event['name'])
    emit('sendEvent', { 'data': getEvent(str(event['id'])) })
    emit('sendEvents', { 'data': getEvents() }, broadcast=True, namespace='/')

@socketio.on('sortir')
def apiAddEvent(event):
    print('sortir: ' + str(event))
    removeUser(event['id'], event['name'])
    emit('sendEvent', { 'data': getEvent(str(event['id'])) })
    emit('sendEvents', { 'data': getEvents() }, broadcast=True, namespace='/')

@socketio.on('generar')
def apiAddEvent(event):
    print('generar: ' + str(event))
    generar(getEvent2(str(event['id'])), event['name'])

@socketio.on('connect', namespace='/')
def test_connect():
    emit('test', {'data': 'Connected'})

if __name__ == '__main__':
    socketio.run(app)
