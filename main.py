
import user_input as ui
import task_manager as tm

if __name__ == "__main__":
    task_option = ui.user_input()
    tm.display_tasks(task_option)