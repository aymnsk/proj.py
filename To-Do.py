tasks = []

def show_tasks():
    for i, task in enumerate(tasks, 1):
        status = "✔" if task["done"] else "✘"
        print(f"{i}. {task['task']} [{status}]")

while True:
    print("\n--- To-Do List ---")
    print("1. Add Task\n2. Show Tasks\n3. Mark Done\n4. Remove Task\n5. Exit")
    choice = int(input("Enter choice: "))

    match choice:
        case 1:
            task = input("Enter task: ")
            tasks.append({"task": task, "done": False})
        case 2:
            show_tasks()
        case 3:
            show_tasks()
            index = int(input("Enter task no to mark done: ")) - 1
            tasks[index]["done"] = True
        case 4:
            show_tasks()
            index = int(input("Enter task no to remove: ")) - 1
            tasks.pop(index)
        case 5:
            break
