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

# Function to auto-increment id for new tasks
def get_next_id():
    #import pdb;pdb.set_trace()
    tasks = load_tasks()

    if not tasks: # if no tasks in the list
        return 1

    max_id = max(task['id'] for task in tasks)
    print(f"Next id is {max_id}")
    return int(max_id) + 1
