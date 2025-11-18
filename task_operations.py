import datetime
import sys
import random

from models.task import Task
from storage import DATA_FILE

def create_task():

    task_id = get_id()

    # Walrus operator allows you to assign a value and use it in an expression simoultaneously
    while len(description := input('Enter a brief description: ')) > 30:
        print('Description too long')

    valid_status = {"todo", "in_progress", "done"}
    while(status := input('Enter status of task("todo", "in-progress", "done"): ')) not in valid_status:
        print("Invalid status. Must be: todo, in-progress, done")

    #set created/updated at using the datetime module
    created_at = datetime.datetime.now()
    updated_at = datetime.datetime.now()

    print(f"\nTask {task_id} created:")
    print(f"  Created At: {created_at}")
    print(f"  Description: {description}")
    print(f"  Status: {status}")

    task = Task(task_id, description, status, created_at, updated_at)
    return task

def update_tasks(task_object):

    valid_status = {"todo", "in_progress", "done"}
    while(new_status := input('Rewrite status: ')) not in valid_status:
        print("Invalid status. Must be: todo, in-progress, done")
    task_object.status = new_status
    task_object.updated_at = datetime.datetime.now()

    return task_object

def display_tasks(task_dict):

    print(f"""
    Task ID: {str(task_dict['id'])}
    Description: {str(task_dict['description'])}
    Status: {str(task_dict['status'])}
    Created At: {str(task_dict['created_at'])}
    Updated At: {str(task_dict['updated_at'])}
    --------------------------
    """)


def quit_program():
    sys.exit()

#Helper function
def get_id():
    #lazy import - import task_manager function where it's need (get_id)
    from task_manager import pass_task_id
    return pass_task_id()