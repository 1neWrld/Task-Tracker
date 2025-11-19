import json
#ensures file path is set on all systems
from pathlib import Path

#import pdb; pdb.set_trace()

DATA_FILE = Path("data/tasks.json")

def load_tasks():

    if not DATA_FILE.exists():
        return [] # no file return empty list

    with open(DATA_FILE, 'r') as f:
        data = json.load(f) # load existing tasks

    # Ensure the result is ALWAYS a list
    if isinstance(data, dict):
        return [data]
    elif isinstance(data, list):
            return data
    else:
        return []


def save_tasks(task_object):

    tasks = load_tasks() # loads existing tasks (a list)

    tasks.append(task_object.to_dict()) # add new task

    with open(DATA_FILE, 'w') as f: # save new task list
        json.dump(tasks, f, indent=4)

#overwrite existing task in json
def update_task(task_object):

    if not DATA_FILE.exists():
        return False

    #load all tasks into the buffer
    with open(DATA_FILE, 'r') as f:
        tasks = json.load(f)

    #replace old dict with new one
    updated = False
    #enumerate connects a counter to an iterable( creates, an enumerate object). apply in loops, access both the index and the value
    for i, task_dict in enumerate(tasks):
        if task_dict.get('id') == task_object.task_id:
            tasks[i] = task_object.to_dict()
            updated = True

    #write updated list back
    if updated:
        with open(DATA_FILE, 'w') as f:
            json.dump(tasks, f, indent=4)

    return updated

def remove_task_from_list(task_id):

    if not DATA_FILE.exists():
        return False

    tasks = load_tasks()

    #filter pattern
    new_tasks = [t for t in tasks if t['id'] != task_id]
    if len(new_tasks) == len(tasks):
        return False

    #for i, task_dict in enumerate(tasks):
        #if(task_dict.get('id') == task_id):
            #del tasks[i]
            #removed = True
            #break

    with open(DATA_FILE, 'w') as f:
        json.dump(new_tasks, f, indent=4)

    return True

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


def get_status_specified_list(status_specified_list):
    tasks = load_tasks()

    #return original list if user prompts to display all tasks
    if status_specified_list == 'all tasks':
        return tasks
    else:
        # create new list containing only status specified tasks
        new_list = [t for t in tasks if t['status'] == status_specified_list]
        if len(new_list) == len(tasks):
            return None
        return new_list

