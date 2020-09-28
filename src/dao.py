from pathlib import Path
from json.decoder import JSONDecodeError
import json

root_dir = Path(__file__).parent.parent
data_file = root_dir / 'data' / 'tasks.json'

def read_task_list_file_contents():
    task_list = []
    with data_file.open('a+') as file:
        try:
            file.seek(0)
            task_list = json.load(file)
        except JSONDecodeError:
            pass
    return task_list

def write_task_list_file(task_list):
    with data_file.open("w") as file:
        json.dump(task_list, file, indent=4)

def delete_all_tasks():
    with data_file.open("w") as file:
        pass