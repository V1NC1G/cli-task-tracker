from datetime import datetime


class TaskManager:

    def __init__(self, tasks=[]):
        self.tasks = tasks
        self.id = 1

    def check_least_id_value(self):
        sorted_list = sorted(self.tasks, key=lambda d: d["id"])
        self.tasks = sorted_list
        counter = 1
        for task_item in self.tasks:
            if task_item["id"] != counter:
                self.id = counter
                return
            else:
                counter += 1

        self.id = counter

    def add_task(self, description: str):
        self.check_least_id_value()
        task_item = {
            "id": self.id,
            "description": description,
            "status": "todo",
            "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "updated_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }

        self.id += 1
        self.tasks.append(task_item)

        print(f"Task successfully added (ID:{task_item['id']})")
        return

    def update_task(self, id: int, description: str):
        task = self.get_task_by_id(id)
        if task:
            task["description"] = description
            print(f"Task (ID: {id}) updated")
            return
        else:
            self.action_non_existing_task(id)

    def delete_task(self, id: int):
        task = self.get_task_by_id(id)
        if task:
            self.tasks.remove(task)
            print(f"Deleted task (ID: {id})")
            return
        else:
            self.action_non_existing_task(id)

    def get_task_by_id(self, id: int):
        for task in self.tasks:
            if task["id"] == id:
                return task
        return None

    def mark_todo(self, id: int):
        task = self.get_task_by_id(id)
        if task:
            task["status"] = "todo"
            print(f"Marked task (ID: {id}) as TODO.")
            return
        else:
            self.action_non_existing_task(id)

    def mark_in_progress(self, id: int):
        task = self.get_task_by_id(id)
        if task:
            task["status"] = "in progress"
            print(f"Marked task (ID: {id}) as IN PROGRESS.")
            return
        else:
            self.action_non_existing_task(id)

    def mark_done(self, id: int):
        task = self.get_task_by_id(id)
        if task:
            task["status"] = "done"
            print(f"Marked task (ID: {id}) as DONE.")
            return
        else:
            self.action_non_existing_task(id)

    def action_non_existing_task(self, id):
        print(f"Task ID: {id} does not exist.")
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
