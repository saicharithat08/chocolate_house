import sqlite3
from flask import Flask, request, jsonify, send_from_directory

app = Flask(__name__, static_folder="static")

def get_db_connection():
    connection = sqlite3.connect("chocolate_house.db")
    connection.row_factory = sqlite3.Row
    return connection

# Serve the main HTML page
@app.route("/")
def index():
    return send_from_directory(app.static_folder, "index.html")

# Endpoint to get all seasonal flavors
@app.route("/flavors", methods=["GET"])
def get_flavors():
    connection = get_db_connection()
    flavors = connection.execute("SELECT * FROM seasonal_flavors").fetchall()
    connection.close()
    return jsonify([dict(row) for row in flavors])

# Endpoint to add a new flavor
@app.route("/flavors", methods=["POST"])
def add_flavor():
    data = request.get_json()
    name = data.get("name")
    description = data.get("description", "")
    available = data.get("available", True)

    connection = get_db_connection()
    connection.execute(
        "INSERT INTO seasonal_flavors (name, description, available) VALUES (?, ?, ?)",
        (name, description, available)
    )
    connection.commit()
    connection.close()
    return jsonify({"message": "Flavor added successfully"}), 201

if __name__ == "__main__":
    app.run(debug=True)
