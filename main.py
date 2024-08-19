import os
import json
from task_manager import TaskManager


def read_tasks_json():
    with open("./tasks.json", "r") as file:
        content = file.read()
        tasks_list = json.loads(content)
        return tasks_list


def is_tasks_list_present():
    if os.path.exists("./tasks.json"):
        return True
    else:
        return False


def populate_tasks(tasks):
    with open("./tasks.json", "w") as file:
        data = json.dumps(tasks)
        file.write(data)


def main():
    if is_tasks_list_present():
        tasks_list = read_tasks_json()
        task_manager = TaskManager(tasks_list)
    else:
        task_manager = TaskManager()

    while True:
        command = input("Command: ")
        action = command.split()[0]

        if action == "add":
            description = " ".join(command.split()[1:])
            task_manager.add_task(description)

        elif action == "update":
            id = int(command.split()[1])
            description = " ".join(command.split()[2:])
            task_manager.update_task(id, description)

        elif action == "delete":
            id = int(command.split()[1])
            task_manager.delete_task(id)

        elif action == "mark-todo":
            id = int(command.split()[1])
            task_manager.mark_todo(id)

        elif action == "mark-in-progress":
            id = int(command.split()[1])
            task_manager.mark_in_progress(id)

        elif action == "mark-done":
            id = int(command.split()[1])
            task_manager.mark_done(id)

        elif action == "list":
            task_manager.list_task()

        elif action == "list-todo":
            task_manager.list_todo()

        elif action == "list-in-progress":
            task_manager.list_in_progress()

        elif action == "list-done":
            task_manager.list_done()

        elif action == "end":
            populate_tasks(task_manager.tasks)
            print("Ending task manager program...")
            return False

        else:
            print(f"Action: {action} is not defined")


if __name__ == "__main__":
    main()
