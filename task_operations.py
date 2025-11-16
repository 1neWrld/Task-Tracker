import datetime
import sys
import random

current_id = 0

def create_task():

    global current_id
    current_id += 1
    task_id = current_id

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

def remove_task():
    print('Remove a task')

def update_task():
    print('Update a task')

def display_task():
    print('Display a task')

def quit_program():
    sys.exit()