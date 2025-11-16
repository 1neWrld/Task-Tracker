import json
#ensures file path is set on all systems
from pathlib import Path

DATA_FILE = Path("data/tasks.json")


def store_tasks(task_object):
    print('Storing tasks...')
    tasks = load_tasks()
    tasks.append(task_object.to_dict())
    save_tasks(tasks)


def load_tasks():
    print('Loading tasks...')

    if DATA_FILE.exists():
        return []

    with open(DATA_FILE, 'r') as f:
        return json.load(f)


def save_tasks(task_object):
    print('Saving tasks...')
    with open(DATA_FILE, 'w') as f:
        json.dump(task_object, f, indent=4)
