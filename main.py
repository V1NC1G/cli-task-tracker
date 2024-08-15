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
        print(task)
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

    def list_task(self):
        for task_item in self.tasks:
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
        elif action == "list":
            task_manager.list_task()
        elif action == "end":
            print("Ending task manager program...")
            return False


if __name__ == "__main__":
    main()
