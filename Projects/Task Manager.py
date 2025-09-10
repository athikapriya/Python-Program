tasks = []

def add_task():
    task_name = input("Enter task: ")
    tasks.append({"task": task_name, "done": False})
    print("Task added!")


def view_tasks():
    if not tasks:
        print("No tasks yet.")
    else:
        for i, task in enumerate(tasks, start=1):
            status = "✔" if task["done"] else "✗"
            print(f"{i}. [{status}] {task['task']}")

def mark_task():
    view_tasks()
    task_num = int(input("Enter task number to mark as done: "))
    if 1 <= task_num <= len(tasks):
        tasks[task_num - 1]["done"] = True
        print("Task marked as completed!")

def delete_task():
    view_tasks()
    task_num = int(input("Enter task number to delete: "))
    if 1 <= task_num <= len(tasks):
        tasks.pop(task_num - 1)
        print("Task deleted!")

def main():
    while True:
        print("\n--- To-Do List ---")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task Completed")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_task()
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            mark_task()
        elif choice == "4":
            delete_task()
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice, try again.")

if __name__ == "__main__":
    main()
