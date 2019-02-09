from flask import Flask
from mongo import getEvents, addEvent
from flask_socketio import SocketIO
from flask_cors import CORS

app = Flask(__name__)
app.config['SECRET_KEY'] = 'holabondiasomhackathon'
# cors = CORS(app)
cors = CORS(app, resources={r"/*":{"origins":"*:*"}})
socketio = SocketIO(app)
socketio.run(app)

@app.route('/api/events')
def apiGetEvents():
    return getEvents()

@app.route('/api/events/add')
def apiAddEvent():
    return addEvent('')

@socketio.on('message')
def handle_message(message):
    print('received message: ' + message)

@socketio.on('connect', namespace='/')
def test_connect():
    emit('test', {'data': 'Connected'})

if __name__ == '__main__':
    socketio.run(app)
