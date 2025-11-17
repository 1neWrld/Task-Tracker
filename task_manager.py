#import module and assign an alias
from codecs import replace_errors

import user_input as ui
import task_operations as task_op
import storage as storage
from storage import find_task_by_id


#import pdb; pdb.set_trace()

def display_tasks(option):
    match option:
        case 1:
            print('==========================')
            print(f"Option {option}: Create a task")
            print('==========================')
            task = task_op.create_task()
            storage.save_tasks(task)
            
        case 2:
            print('==========================')
            print(f"Option {option}: Remove a task")
            print('==========================')

            task_op.remove_task()

        case 3:
            print('==========================')
            print(f"Option {option}: Update a task")
            print('==========================')

            task_id = int(input('Enter task id: '))
            task_object = pass_task(task_id)

            if not task_object:
                print('Task not found')
            else:
                updated_task = task_op.update_tasks(task_object)
                storage.update_task(updated_task)


        case 4:
            print('==========================')
            print(f"Option {option}: Display a task")
            print('==========================')
            task_op.display_task()
        case 5:
            print('==========================')
            print('Quit, Goodbye')
            print('==========================')
            task_op.quit_program()
        case _:
            print('Option not recognized')

#pass through function
def pass_task_id():
    _id = storage.get_next_id()
    return _id

# find task by id in List[Dict], convert and return task instance
def pass_task(task_id):
    from models.task import Task

    #get and store task dict
    task = find_task_by_id(task_id)

    if task is None:
        return None

    #return converted task (dict) to task instance/object
    return Task.from_dict(task)


