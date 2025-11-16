#import module and assign an alias
import user_input as ui
import task_operations as task_op
import storage as storage

def display_tasks(option):
    match option:
        case 1:
            print('==========================')
            print('Option',option, ': Create a task')
            print('==========================')
            task = task_op.create_task()
            storage.store_tasks(task)
            
        case 2:
            print('==========================')
            print('Option',option, ': Remove a task')
            print('==========================')
            task_op.remove_task()
        case 3:
            print('==========================')
            print('Option',option, ': Update a task')
            print('==========================')
            task_op.update_task()
        case 4:
            print('==========================')
            print('Option',option, ': Display a task')
            print('==========================')
            task_op.display_task()
        case 5:
            print('==========================')
            print('Quit, Goodbye')
            print('==========================')
            task_op.quit_program()
        case _:
            print('Option not recognized')



task_option = ui.user_input()
display_tasks(task_option)
