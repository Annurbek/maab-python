import json
import csv
import os

class Tasks:
    def __init__(self, task_id, task_name, task_description, date_line, status):
        self.task_id = task_id
        self.task_name = task_name
        self.task_description = task_description
        self.date_line = date_line
        self.status = status
    
    def __str__(self):
        return f"{self.task_id}, {self.task_name}, {self.task_description}, {self.date_line}, {self.status}"
    
    def to_line(self):
        return f"{self.task_id},{self.task_name},{self.task_description},{self.date_line},{self.status}\n"
    
    def to_dict(self):
        return {
            "task_id": self.task_id,
            "task_name": self.task_name,
            "task_description": self.task_description,
            "date_line": self.date_line,
            "status": self.status
        }

    @staticmethod
    def from_line(line):
        parts = line.strip().split(",")
        return Tasks(parts[0], parts[1], parts[2], parts[3], parts[4])
    
class StorageManage:
    def __init__(self, filename):
        self.filename = filename
        self.extension = os.path.splitext(filename)[1].lower()

    def load_tasks(self):
        if not os.path.exists(self.filename):
            return []
        
        if self.extension == ".json":
             with open(self.filename, "r", encoding="utf-8") as file:
                data = json.load(file)
                return [Tasks(**task) for task in data]
        elif self.extension == ".csv":
            with open(self.filename, newline="", encoding="utf-8") as file:
                reader = csv.DictReader(file)
                return [Tasks(**row) for row in reader]
    
        elif self.extension == ".txt":
            with open(self.filename, "r", encoding="utf-8") as file:
                tasks = []
                for line in file:
                    tasks.append(Tasks.from_line(line))
                return tasks
        else:
            raise ValueError("❌ Поддерживаются только .json, .csv и .txt")
    
    def save_tasks(self, tasks):
        if self.extension == ".json":
            with open(self.filename, "w", encoding="utf-8") as file:
                json.dump([task.to_dict() for task in tasks], file, indent=4)
        
        elif self.extension == ".csv":
            if not tasks:
                return
            with open(self.filename, "w", newline="", encoding="utf-8") as file:
                writer = csv.DictWriter(file, fieldnames=tasks[0].to_dict().keys())
                writer.writeheader()
                writer.writerows([task.to_dict() for task in tasks])
        
        elif self.extension == ".txt":
            with open(self.filename, "w", encoding="utf-8") as file:
                for task in tasks:
                    file.write(task.to_line())
        else:
            raise ValueError("❌ Поддерживаются только .json, .csv и .txt")

class TaskManage:
    def __init__(self, storage):
        self.storage = storage
        self.tasks = self.storage.load_tasks()

    def add_task(self, task):
        if any(t.task_id == task.task_id for t in self.tasks):
            print("❌ Task ID already exists.")
            return
        self.tasks.append(task)
        self.storage.save_tasks(self.tasks)
        print("✅ Task added successfully!")
    
    def view_all_tasks(self):
        if not self.tasks:
            print("⚠️ No tasks records found.")
        else:
            print("📋 Tasks Records:")
            for task in self.tasks:
                print(task)
    
    def search_task(self, task_id):
        for task in self.tasks:
            if task.task_id == task_id:
                return task
        print("⚠️ Task not found.")
        return None
    
    def update_task(self, task_id, task_name=None, task_description=None, 
                   date_line=None, status=None):
        task = self.search_task(task_id)
        if task:
            if task_name:
                task.task_name = task_name
            if task_description:
                task.task_description = task_description
            if date_line:
                task.date_line = date_line
            if status:
                task.status = status
            self.storage.save_tasks(self.tasks)
            print("✅ Task updated.")
        else:
            print("❌ Task not found.")
    
    def delete_task(self, task_id):
        initial_length = len(self.tasks)
        self.tasks = [task for task in self.tasks if task.task_id != task_id]
        
        if len(self.tasks) < initial_length:
            self.storage.save_tasks(self.tasks)
            print("✅ Task deleted.")
        else:
            print("❌ Task not found.")

    def filter_by_status(self, status):
        filtered_tasks = [task for task in self.tasks if task.status.lower() == status.lower()]
        if not filtered_tasks:
            print(f"⚠️ No tasks found with status: {status}")
        else:
            print(f"📋 Tasks with status '{status}':")
            for task in filtered_tasks:
                print(task)
        return filtered_tasks
    
    def main(self):
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
                task_id = input("Enter task ID: ")
                task_name = input("Enter task name: ")
                task_description = input("Enter task description: ")
                date_line = input("Enter deadline: ")
                status = input("Enter status: ")
                new_task = Tasks(task_id, task_name, task_description, date_line, status)
                self.add_task(new_task)
            elif choice == "2":
                self.view_all_tasks()
            elif choice == "3":
                task_id = input("Enter task ID to update: ")
                task_name = input("Enter new task name (or press Enter to skip): ")
                task_description = input("Enter new task description (or press Enter to skip): ")
                date_line = input("Enter new deadline (or press Enter to skip): ")
                status = input("Enter new status (or press Enter to skip): ")
                self.update_task(task_id, task_name or None, task_description or None,
                               date_line or None, status or None)
            elif choice == "4":
                task_id = input("Enter task ID to delete: ")
                self.delete_task(task_id)
            elif choice == "5":
                status = input("Enter status to filter by: ")
                self.filter_by_status(status)
            elif choice == "6":
                self.storage.save_tasks(self.tasks)
                print("✅ Tasks saved successfully!")
            elif choice == "7":
                self.tasks = self.storage.load_tasks()
                print("✅ Tasks loaded successfully!")
            elif choice == "8":
                print("Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    storage = StorageManage("tasks.json")
    task_manager = TaskManage(storage)
    task_manager.main()