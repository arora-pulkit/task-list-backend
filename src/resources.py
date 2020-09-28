from flask import Flask, jsonify, request
from dao import *


app = Flask(__name__)

@app.route('/tasks', methods=['GET'])
def get_tasks():
  task_list = read_task_list_file_contents()
  return jsonify(task_list)

@app.route('/task', methods=['POST'])
def add_task():
  current_task_list = read_task_list_file_contents()
  new_task = request.get_json()
  new_task.update({"id": len(current_task_list) + 1})
  current_task_list.append(new_task)
  write_task_list_file(current_task_list)
  return "Success", 200

@app.route('/tasks', methods=['DELETE'])
def delete_tasks():
  delete_all_tasks()
  return "Success", 200