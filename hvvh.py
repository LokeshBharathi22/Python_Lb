from flask import Flask, request, jsonify
from flask_pymongo import PyMongo
from flask_bcrypt import Bcrypt

app = Flask(__name__)
app.config['MONGO_URI'] = 'mongodb://localhost:27017/whatsapp_clone'
mongo = PyMongo(app)
bcrypt = Bcrypt(app)

@app.route('/register', methods=['POST'])
def register():
    data = request.json
    username = data.get('username')
    password = data.get('password')

    existing_user = mongo.db.users.find_one({'username': username})
    if existing_user:
        return jsonify({'message': 'Username already exists'}), 400

    hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
    mongo.db.users.insert_one({'username': username, 'password': hashed_password})
    return jsonify({'message': 'User registered successfully'}), 201

@app.route('/login', methods=['POST'])
def login():
    data = request.json
    username = data.get('username')
    password = data.get('password')

    user = mongo.db.users.find_one({'username': username})
    if not user or not bcrypt.check_password_hash(user['password'], password):
        return jsonify({'message': 'Invalid username or password'}), 401

    # Here you would typically generate a JWT token for authentication
    return jsonify({'message': 'Login successful'}), 200

@app.route('/message', methods=['POST'])
def send_message():
    data = request.json
    sender = data.get('sender')
    receiver = data.get('receiver')
    content = data.get('content')

    mongo.db.messages.insert_one({'sender': sender, 'receiver': receiver, 'content': content})
    return jsonify({'message': 'Message sent successfully'}), 201

@app.route('/messages/<user_id>', methods=['GET'])
def get_messages(user_id):
    messages = list(mongo.db.messages.find({'$or': [{'sender': user_id}, {'receiver': user_id}]}))
    return jsonify({'messages': messages}), 200

if __name__ == '__main__':
    app.run(debug=True)
