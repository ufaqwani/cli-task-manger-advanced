import json
import os

TASK_FILE = "tasks.json"

def save_tasks_to_file(tasks):  # receive tasks as argument
    with open(TASK_FILE, "w") as file:
        json.dump(tasks, file)

def load_tasks_from_file():  # return the list instead of modifying a global
    if os.path.exists(TASK_FILE):
        with open(TASK_FILE, "r") as file:
            try:
                loaded = json.load(file)
                if isinstance(loaded, list):
                    return loaded
                else:
                    print("Invalid format. Starting fresh.")
                    return []
            except json.JSONDecodeError:
                print("Corrupted task file. Starting fresh.")
                return []
    return []
