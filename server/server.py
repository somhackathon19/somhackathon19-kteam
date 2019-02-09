from flask import Flask
from mongo import getEvents
from flask_socketio import SocketIO

app = Flask(__name__)
app.config['SECRET_KEY'] = 'holabondiasomhackathon'
socketio = SocketIO(app)

@app.route('/api/events')
def apiGetEvents():
    return getEvents()

@socketio.on('message')
def handle_message(message):
    print('received message: ' + message)

if __name__ == '__main__':
    socketio.run(app)
