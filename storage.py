import json
#ensures file path is set on all systems
from pathlib import Path

#import pdb; pdb.set_trace()

DATA_FILE = Path("data/tasks.json")

def load_tasks():
    print('Loading tasks...')

    if not DATA_FILE.exists():
        return [] # no file return empty list

    with open(DATA_FILE, 'r') as f:
        data = json.load(f) # load existing tasks

    if isinstance(data, dict): #if file contains dictionary return list
        if not data: # if empty dict return empty list
            return []
        return [data]

    return data


def save_tasks(task_object):
    print('Saving tasks...')

    tasks = load_tasks() # loads existing tasks (a list)

    tasks.append(task_object.to_dict()) # add new task

    with open(DATA_FILE, 'w') as f: # save new task list
        json.dump(tasks, f, indent=4)

#overwrite existing task in json
def update_task(task_object):
    print('Updating tasks...')

    if not DATA_FILE.exists():
        return False

    #load all tasks into the buffer
    with open(DATA_FILE, 'r') as f:
        tasks = json.load(f)

    #replace old dict with new one
    updated = False
    for i, task_dict in enumerate(tasks):
        if task_dict.get('id') == task_object.task_id:
            tasks[i] = task_object.to_dict()
            updated = True

    #write updated list back
    if updated:
        with open(DATA_FILE, 'w') as f:
            json.dump(tasks, f, indent=4)

    return updated


# Function to auto-increment id for new tasks
def get_next_id():
    #import pdb;pdb.set_trace()
    tasks = load_tasks()

    if not tasks: # if no tasks in the list (empty list)
        return 1

    max_id = max(task['id'] for task in tasks)
    return int(max_id) + 1

def find_task_by_id(task_id):
    tasks = load_tasks()
    for task in tasks:
        if task['id'] == task_id:
            return task
    return None

