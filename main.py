from datetime import datetime

print("Actions:")
print("add <Item/Task>")
print("update <Item/Task>")
print("delete <Item/Task>")
print("\n")

id = 0


def user_input():
    user_input = input("What do you want to do?: ")
    action = user_input.split()[0]
    task = " ".join(user_input.split()[1:])
    print(f"Action: {action}")
    print(f"Task: {task}")

    if action == "add":
        add_task(action, task)

    return action, task


def add_task(action, task):
    task_item = {
        "id": id + 1,
        "description": task,
        "status": "todo",
        "createdAt": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "updated_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

    print(task_item)

    return task_item


print(user_input())
