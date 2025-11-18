
def get_task_chosen():
    print('Choose an option for your task')
    print('==========================')
    print('1. Create/Add a task')
    print('2. Remove a task')
    print('3. Update a task status')
    print('4. Display tasks')
    print('5. Quit')
    print('==========================')

    while True:
        try:
            choice = int(input('Please enter a number between 1 and 5: '))
            if 1 <= choice <= 5:
                return choice
            else:
                print('Please enter a number between 1 and 5: ')
        except ValueError:
            print('Invalid option. Please enter a valid choice')
    return choice

def user_input():
   choice = get_task_chosen()
   match choice:
       case 1:
          return 1
       case 2:
           return 2
       case 3:
           return 3
       case 4:
           return 4
       case 5:
           return 5
       case _:
           return 'Please enter a valid choice'
