from flask import Flask, jsonify
from flask_cors import CORS
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, render_template, request
from sqlalchemy import text
import os 

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(os.path.dirname(__file__), 'taskmanager.db')
db = SQLAlchemy(app)

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String)
    password= db.Column(db.Integer)
    
    
    def __init__(self, id, email, password,):
        self.id = id
        self.email = email
        self.total_price = password
        
with app.app_context():
    try:
        db.session.execute(text('SELECT * from users'))
        print("Database connection successful!")
    except Exception as e:
        print("Failed to connect to the database:", str(e))        

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

@app.route('/sign_up', methods=['POST'])
def sign_up():
    json_data = request.get_json()
    print(json_data)
    return make_response ('success')

if __name__ == '__main__':
    app.debug = True
    app.run()
