from flask import Flask, request
from mongo import *
from flask_socketio import SocketIO, send, emit
from flask_cors import CORS

app = Flask(__name__)
app.config['SECRET_KEY'] = 'holabondiasomhackathon'
cors = CORS(app, resources={r"/*":{"origins":"*:*"}})
# cors = CORS(app)
socketio = SocketIO(app)
socketio.run(app)

#######################################################

@app.route('/api/events')
def apiGetEvents():
    return getEvents()

@app.route('/api/event/get/<id>')
def apiGetEvent(id):
    return getEvent(id)

@app.route('/api/event/remove/<id>')
def apiRemoveEvents(id):
    return removeEvent(id)

@socketio.on('addEvent')
def addEvent(event):
    print('new event: ' + str(event))
    addEvent(event)

#######################################################

@socketio.on('connect', namespace='/')
def test_connect():
    emit('test', {'data': 'Connected'})

if __name__ == '__main__':
    socketio.run(app)
