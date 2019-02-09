from flask import Flask
from flask import jsonify
app = Flask(__name__)

events = [
    {
      "id": 1,
      "titol": "bon dia",
      "descripcio": "hola bon dia"
    }
  ]

@app.route('/api/events')
def getEvents():
    return jsonify(events)
