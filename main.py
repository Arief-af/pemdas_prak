from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
from database import get_database_connection

app = Flask(__name__)
CORS(app) 

@app.route("/data", methods=["POST"])
def store():
    data = request.get_json()
    if not data or "humidity" not in data or "temp" not in data:
        return jsonify({"error": "Invalid input"}), 400
    
    humidity = data["humidity"]
    temp = data["temp"]
    
    connection = get_database_connection()
    cursor = connection.cursor()
    query = "INSERT INTO dht_readings (humidity, temp) VALUES (%s, %s)"
    values = (humidity, temp)
    cursor.execute(query, values)
    connection.commit()
    connection.close()
    
    return jsonify({"message": "User created successfully"})

@app.route("/", methods=["GET"])
def read_data():
    connection = get_database_connection()
    cursor = connection.cursor()
    query = "SELECT * FROM dht_readings"
    cursor.execute(query)
    users = cursor.fetchall()
    connection.close()
    
    return render_template("index.html", users=users)

if __name__ == "__main__":
    app.run(debug=True)
