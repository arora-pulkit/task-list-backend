from flask import Flask, jsonify, request
from dao import *
from flask_cors import CORS
import time

app = Flask(__name__)
CORS(app)

@app.route('/tasks', methods=['GET'])
def get_tasks():
  task_list = read_task_list_file_contents()
  response = jsonify(task_list)
  return response

@app.route('/task', methods=['POST'])
def add_task():
  current_task_list = read_task_list_file_contents()
  new_task = request.get_json()
  print("request json : "  + str(new_task))
  id = str(time.time())
  new_task.update({"id": id})
  current_task_list.append(new_task)
  write_task_list_file(current_task_list)
  return id, 200

@app.route('/tasks', methods=['DELETE'])
def delete_tasks():
  delete_all_tasks()
  return "Success", 200

@app.route('/task', methods=['DELETE'])
def delete_task():
  id = request.args.get("id")
  delete_task_by_id(id)
  return "Success", 200