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

    def update_task(self, id, description, status=None):
        task = self.get_task_by_id(id)
        task["description"] = description
        if status:
            task["status"] = status
        return

    def delete_task(self, id):
        task = self.get_task_by_id(id)
        self.task.remove(task)

    def get_task_by_id(self, id):
        for task in self.tasks:
            if task.id == id:
                return task
        return None


def main():
    task_manager = TaskManager()
    while True:
        action = input("Command: ")
        if action == "add":
            task_manager.add_task()


if __name__ == "__main__":
    main()
