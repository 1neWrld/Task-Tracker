import task_manager
import user_input as ui
import task_manager as tm


if __name__ == "__main__":
    while(task_option := ui.user_input()) is not 5:
        tm.chosen_task_operation(task_option)