import json
from datetime import datetime

tasks = {}

def add_task():
    task_id = input("Enter Task ID: ")
    if task_id in tasks:
        print("Task ID already exists.")
        return
    title = input("Enter Title: ")
    description = input("Enter Description: ")
    due_date = input("Enter Due Date (YYYY-MM-DD): ")
    status = input("Enter Status (Pending/In Progress/Completed): ")
    tasks[task_id] = {
        "title": title,
        "description": description,
        "due_date": due_date,
        "status": status
    }
    print("Task added successfully!")

def view_tasks():
    if not tasks:
        print("No tasks found.")
        return
    print("Tasks:")
    for task_id, task in tasks.items():
        print(f"{task_id}, {task['title']}, {task['description']}, {task['due_date']}, {task['status']}")

def update_task():
    task_id = input("Enter Task ID to update: ")
    if task_id not in tasks:
        print("Task not found.")
        return
    print("Leave a field empty to keep the current value.")
    title = input("Enter new Title: ") or tasks[task_id]["title"]
    description = input("Enter new Description: ") or tasks[task_id]["description"]
    due_date = input("Enter new Due Date (YYYY-MM-DD): ") or tasks[task_id]["due_date"]
    status = input("Enter new Status (Pending/In Progress/Completed): ") or tasks[task_id]["status"]
    tasks[task_id].update({
        "title": title,
        "description": description,
        "due_date": due_date,
        "status": status
    })
    print("Task updated successfully!")

def delete_task():
    task_id = input("Enter Task ID to delete: ")
    if task_id in tasks:
        del tasks[task_id]
        print("Task deleted successfully!")
    else:
        print("Task not found.")

def filter_tasks():
    status = input("Enter status to filter by (Pending/In Progress/Completed): ")
    filtered = {tid: t for tid, t in tasks.items() if t["status"].lower() == status.lower()}
    if not filtered:
        print("No tasks found with that status.")
        return
    for task_id, task in filtered.items():
        print(f"{task_id}, {task['title']}, {task['description']}, {task['due_date']}, {task['status']}")

def save_tasks():
    with open("tasks.json", "w") as f:
        json.dump(tasks, f, indent=4)
    print("Tasks saved to tasks.json.")

def load_tasks():
    global tasks
    try:
        with open("tasks.json", "r") as f:
            tasks = json.load(f)
        print("Tasks loaded from tasks.json.")
    except FileNotFoundError:
        print("No saved tasks found.")

def main():
    while True:
        print("\nWelcome to the To-Do Application!")
        print("1. Add a new task")
        print("2. View all tasks")
        print("3. Update a task")
        print("4. Delete a task")
        print("5. Filter tasks by status")
        print("6. Save tasks")
        print("7. Load tasks")
        print("8. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            add_task()
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            update_task()
        elif choice == "4":
            delete_task()
        elif choice == "5":
            filter_tasks()
        elif choice == "6":
            save_tasks()
        elif choice == "7":
            load_tasks()
        elif choice == "8":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
