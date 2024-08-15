from datetime import datetime
import json
import string
import random


class TaskManager:

    def __init__(self, tasks=[]):
        self.tasks = tasks
        self.id = 1

    def add_task(self, description):
        task_item = {
            "id": self.id,
            "description": description,
            "status": "todo",
            "createdAt": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "updated_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }

        self.id += 1
        self.tasks.append(task_item)

        print(f"Task successfully added (ID:{task_item['id']})")
        return

    def update_task(self, id, description):
        task = self.get_task_by_id(id)
        task["description"] = description
        print(f"Task (ID: {id}) updated")
        return

    def delete_task(self, id):
        task = self.get_task_by_id(id)
        self.tasks.remove(task)
        print(f"Deleted task (ID: {id})")
        return

    def get_task_by_id(self, id):
        for task in self.tasks:
            if task["id"] == id:
                return task
        return None

    def mark_todo(self, id):
        task = self.get_task_by_id(id)
        task["status"] = "todo"
        print(f"Marked task (ID: {id}) as TODO.")
        return

    def mark_in_progress(self, id):
        task = self.get_task_by_id(id)
        task["status"] = "in progress"
        print(f"Marked task (ID: {id}) as IN PROGRESS.")
        return

    def mark_done(self, id):
        task = self.get_task_by_id(id)
        task["status"] = "done"
        print(f"Marked task (ID: {id}) as DONE.")
        return

    def list_task(self):
        for task_item in self.tasks:
            print("\n")
            print(f"ID: {task_item['id']}")
            print(f"Task: {task_item['description']}")
            print(f"Status: {task_item['status'].upper()}")
            print("\n")
        return

    def list_todo(self):
        for task_item in self.tasks:
            if task_item["status"] == "todo":
                print("\n")
                print(f"ID: {task_item['id']}")
                print(f"Task: {task_item['description']}")
                print(f"Status: {task_item['status'].upper()}")
                print("\n")
        return

    def list_in_progress(self):
        for task_item in self.tasks:
            if task_item["status"] == "in progress":
                print("\n")
                print(f"ID: {task_item['id']}")
                print(f"Task: {task_item['description']}")
                print(f"Status: {task_item['status'].upper()}")
                print("\n")
        return

    def list_done(self):
        for task_item in self.tasks:
            if task_item["status"] == "done":
                print("\n")
                print(f"ID: {task_item['id']}")
                print(f"Task: {task_item['description']}")
                print(f"Status: {task_item['status'].upper()}")
                print("\n")
        return


def main():
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
            print("Ending task manager program...")
            return False


if __name__ == "__main__":
    main()
