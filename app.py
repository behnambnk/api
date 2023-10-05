from flask import Flask, jsonify, request, make_response
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text
import os 

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(os.path.dirname(__file__), 'taskmanager.db')
db = SQLAlchemy(app)

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String)
    password = db.Column(db.Integer)  
    
    def __init__(self, email, password):
        self.email = email
        self.password = password

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    
    def __init__(self, name):
        self.name = name
        



        
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

@app.route('/tasks', methods=['POST'])
def get_tasks():
     json_data = request.get_json()

     name = json_data.get('name')


@app.route('/sign_up', methods=['POST'])
def sign_up():
    json_data = request.get_json()
    
   
    email = json_data.get('email')
    password = json_data.get('password')

    if not email or not password:
        return make_response(jsonify({'error': 'Email and password are required.'}), 400)

    
    new_user = User(email=email, password=password)
    db.session.add(new_user)
    db.session.commit()

    return make_response(jsonify({'message': 'User created successfully!'}), 201)





if __name__ == '__main__':
    app.debug = True
    app.run()
