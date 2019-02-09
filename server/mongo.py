from flask import jsonify

def getEvents():
    events = [
        {
            "id": 1,
            "titol": "bon dia",
            "descripcio": "hola bon dia"
        }
    ]
    return jsonify(events)