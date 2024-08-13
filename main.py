from datetime import datetime
import json

print("Actions:")
print("add <Item/Task>")
print("update <Item/Task>")
print("delete <Item/Task>")
print("\n")

data = {
    "tasks": []
}

id = 0

with open("./tasks.json", "w"):
    print("created a file")


def user_input():
    user_input = input("What do you want to do?: ")
    action = user_input.split()[0]
    task = " ".join(user_input.split()[1:])
    print(f"Action: {action}")
    print(f"Task: {task}")

    if action == "add":
        new_task = json.dumps(add_task(task))
        with open("tasks.json", "w") as file:
            file.write(new_task)

    return action, task


def add_task(task):
    task_item = {
        "id": id + 1,
        "description": task,
        "status": "todo",
        "createdAt": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "updated_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

    print(f"Task successfully added (ID:{task_item['id']})")

    return task_item


def update_task(task_id, task):
    for task_item in data["tasks"]:
        if task_item.id == task_id:
            task_item["description"] = task
            task_item["updated_at"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    print(f"Updated Task ID:{task_id}")
    return 


def delete_task(task_id):
    for task_item in data["tasks"]:
        if task_item.id == task_id:
            # remove item
            return

    return

print(user_input())
