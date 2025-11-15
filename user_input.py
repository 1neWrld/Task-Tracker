
def user_input():
   choice = get_task_chosen()
   match choice:
       case 1:
           print('1. Create a new task')
           return 1
       case 2:
           print('2. Update a task')
           return 2
       case 3:
           print('3. Delete a task')
           return 3
       case 4:
           print('4. Display all tasks')
           return 4
       case 5:
           print('5. Quit')
           return 5
       case _:
           return 'Please enter a valid choice'

def get_task_chosen():
    print('Choose an option for your task')
    print('==========================')
    print('1. Create/Add a task')
    print('2. Update a task')
    print('3. Delete a task')
    print('3. Remove a task')
    print('4. Display all tasks')
    print('5. Quit')
    print('==========================')
    choice = int(input('enter your choice(1 - 4): '))

    return choice