from flask import Flask, jsonify
import sqlite3

app = Flask(__name__)


@app.route('/')
def index():
    return "Flask REST API by Whilmar Bitoco"

@app.route('/users', methods=['GET'])
def get_users():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM user")
    rows = cursor.fetchall()
    user_list = []
    for row in rows:
        user_dict = {}
        user_dict['id'] = row[0]
        user_dict['name'] = row[1]
        user_dict['gender'] = row[2]
        user_dict['age'] = row[3]
        user_list.append(user_dict)
    conn.close()
    return jsonify(user_list)

@app.route('/users/<int:id>', methods=['GET'])
def get_user(id):
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM user WHERE id=?", (id,))
    row = cursor.fetchone()
    conn.close()
    if row is None:
        return jsonify({'error': 'User not found'})
    user_dict = {
        'id': row[0],
        'name': row[1],
        'gender': row[2],
        'age': row[3]
    }
    return jsonify(user_dict)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=81)
