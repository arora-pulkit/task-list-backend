from flask import Flask, jsonify
app = Flask(__name__)

tasks = [
  { 'description': 'Email Satya', 'deadline': "today"}
]

@app.route("/tasks", methods=['GET'])
def get_tasks():
  return jsonify(tasks)