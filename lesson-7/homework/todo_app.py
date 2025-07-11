import json
import csv
import os
from datetime import datetime

class Task:
    def __init__(self, task_id, title, description, due_date, status):
        self.task_id = task_id
        self.title = title
        self.description = description
        self.due_date = due_date
        self.status = status

    def to_dict(self):
        return {
            "task_id": self.task_id,
            "title": self.title,
            "description": self.description,
            "due_date": self.due_date,
            "status": self.status
        }

    @staticmethod
    def from_dict(d):
        return Task(d["task_id"], d["title"], d["description"], d["due_date"], d["status"])

class TaskStorage:
    def save(self, tasks):
        raise NotImplementedError

    def load(self):
        raise NotImplementedError

class JSONTaskStorage(TaskStorage):
    def __init__(self, filename="tasks.json"):
        self.filename = filename

    def save(self, tasks):
        with open(self.filename, "w") as f:
            json.dump([task.to_dict() for task in tasks.values()], f, indent=4)
        print(f"Tasks saved to {self.filename}.")

    def load(self):
        if not os.path.exists(self.filename):
            return {}
        with open(self.filename, "r") as f:
            data = json.load(f)
            return {d["task_id"]: Task.from_dict(d) for d in data}

class CSVTaskStorage(TaskStorage):
    def __init__(self, filename="tasks.csv"):
        self.filename = filename

    def save(self, tasks):
        with open(self.filename, "w", newline='') as f:
            writer = csv.DictWriter(f, fieldnames=["task_id", "title", "description", "due_date", "status"])
            writer.writeheader()
            for task in tasks.values():
                writer.writerow(task.to_dict())
        print(f"Tasks saved to {self.filename}.")

    def load(self):
        if not os.path.exists(self.filename):
            return {}
        with open(self.filename, "r", newline='') as f:
            reader = csv.DictReader(f)
            return {row["task_id"]: Task.from_dict(row) for row in reader}

class ToDoApp:
    def __init__(self, storage: TaskStorage):
        self.storage = storage
        self.tasks = self.storage.load()

    def add_task(self):
        task_id = input("Enter Task ID: ")
        if task_id in self.tasks:
            print("Task ID already exists.")
            return
        title = input("Enter Title: ")
        description = input("Enter Description: ")
        due_date = input("Enter Due Date (YYYY-MM-DD): ")
        status = input("Enter Status (Pending/In Progress/Completed): ")
        self.tasks[task_id] = Task(task_id, title, description, due_date, status)
        print("Task added successfully!")

    def view_tasks(self):
        if not self.tasks:
            print("No tasks found.")
            return
        print("Tasks:")
        for task in self.tasks.values():
            print(f"{task.task_id}, {task.title}, {task.description}, {task.due_date}, {task.status}")

    def update_task(self):
        task_id = input("Enter Task ID to update: ")
        if task_id not in self.tasks:
            print("Task not found.")
            return
        print("Leave a field empty to keep the current value.")
        task = self.tasks[task_id]
        title = input("Enter new Title: ") or task.title
        description = input("Enter new Description: ") or task.description
        due_date = input("Enter new Due Date (YYYY-MM-DD): ") or task.due_date
        status = input("Enter new Status (Pending/In Progress/Completed): ") or task.status
        self.tasks[task_id] = Task(task_id, title, description, due_date, status)
        print("Task updated successfully!")

    def delete_task(self):
        task_id = input("Enter Task ID to delete: ")
        if task_id in self.tasks:
            del self.tasks[task_id]
            print("Task deleted successfully!")
        else:
            print("Task not found.")

    def filter_tasks(self):
        status = input("Enter status to filter by (Pending/In Progress/Completed): ")
        filtered = [t for t in self.tasks.values() if t.status.lower() == status.lower()]
        if not filtered:
            print("No tasks found with that status.")
            return
        for task in filtered:
            print(f"{task.task_id}, {task.title}, {task.description}, {task.due_date}, {task.status}")

    def save_tasks(self):
        self.storage.save(self.tasks)

    def load_tasks(self):
        self.tasks = self.storage.load()
        print("Tasks loaded.")

    def main_menu(self):
        while True:
            print("\nWelcome to the To-Do Application!")
            print("1. Add a new task")
            print("2. View all tasks")
            print("3. Update a task")
            print("4. Delete a task")
            print("5. Filter tasks by status")
            print("6. Save tasks")
            print("7. Load tasks")
            print("8. Switch storage format")
            print("9. Exit")
            choice = input("Enter your choice: ")
            if choice == "1":
                self.add_task()
            elif choice == "2":
                self.view_tasks()
            elif choice == "3":
                self.update_task()
            elif choice == "4":
                self.delete_task()
            elif choice == "5":
                self.filter_tasks()
            elif choice == "6":
                self.save_tasks()
            elif choice == "7":
                self.load_tasks()
            elif choice == "8":
                self.switch_storage()
            elif choice == "9":
                print("Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")

    def switch_storage(self):
        print("Select storage format:")
        print("1. JSON")
        print("2. CSV")
        fmt = input("Enter your choice: ")
        if fmt == "1":
            self.storage = JSONTaskStorage()
        elif fmt == "2":
            self.storage = CSVTaskStorage()
        else:
            print("Invalid choice.")
            return
        self.load_tasks()

if __name__ == "__main__":
    app = ToDoApp(JSONTaskStorage())
    app.main_menu()
