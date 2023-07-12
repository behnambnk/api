from flask import Flask, jsonify

app = Flask(__name__)

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

@app.route('/task/<int:task_id>')
def get_task(task_id):
    task = next((task for task in tasks if task['id'] == task_id), None)
    if task:
        return jsonify(task)
    else:
        return jsonify({'error': 'Task not found'})

if __name__ == '__main__':
    app.run()
