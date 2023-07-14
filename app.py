from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)

CORS(app)

tasks = [
    {
        'id': 1,
        'name': 'Set a reminder beforehand',
    },
    {
        'id': 2,
        'name': 'Find a location',
    },
    {
        'id': 3,
        'name': 'Screenshot the address',
    },
    {
        'id': 4,
        'name': 'Book the tickets',
    },
    {
        'id': 5,
        'name': 'Find out the parking',
    }
]

@app.route('/tasks')
def get_tasks():
    return jsonify(tasks)



if __name__ == '__main__':
    app.debug = True
    app.run()
