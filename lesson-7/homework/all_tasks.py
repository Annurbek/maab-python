# =========================
# task 1: Generalized Vector Class
# =========================
import math

class Vector:
    def __init__(self, *args):
        self.components = tuple(args)

    def __str__(self):
        return f"Vector{self.components}"

    def __add__(self, other):
        if not isinstance(other, Vector) or len(self.components) != len(other.components):
            raise ValueError("Vectors must have the same dimensions")
        return Vector(*(a + b for a, b in zip(self.components, other.components)))

    def __sub__(self, other):
        if not isinstance(other, Vector) or len(self.components) != len(other.components):
            raise ValueError("Vectors must have the same dimensions")
        return Vector(*(a - b for a, b in zip(self.components, other.components)))

    def __mul__(self, other):
        if isinstance(other, Vector):
            if len(self.components) != len(other.components):
                raise ValueError("Vectors must have the same dimensions")
            return sum(a * b for a, b in zip(self.components, other.components))
        elif isinstance(other, (int, float)):
            return Vector(*(a * other for a in self.components))
        else:
            return NotImplemented

    def __rmul__(self, other):
        return self.__mul__(other)

    def __truediv__(self, scalar):
        if scalar == 0:
            raise ValueError("Cannot divide by zero")
        return Vector(*(a / scalar for a in self.components))

    def magnitude(self):
        return math.sqrt(sum(a ** 2 for a in self.components))

    def normalize(self):
        mag = self.magnitude()
        if mag == 0:
            raise ValueError("Cannot normalize zero vector")
        return Vector(*(round(a / mag, 3) for a in self.components))

# Example usage:
# v1 = Vector(1, 2, 3)
# v2 = Vector(4, 5, 6)
# print(v1)
# print(v1 + v2)
# print(v2 - v1)
# print(v1 * v2)
# print(3 * v1)
# print(v1.magnitude())
# print(v1.normalize())

# =========================
# task 2: Employee Records Manager (OOP Version)
# =========================
import os

class Employee:
    def __init__(self, employee_id, name, position, salary):
        self.employee_id = employee_id
        self.name = name
        self.position = position
        self.salary = float(salary)

    def __str__(self):
        return f"{self.employee_id}, {self.name}, {self.position}, {self.salary}"

    def to_line(self):
        return f"{self.employee_id},{self.name},{self.position},{self.salary}\n"

    @staticmethod
    def from_line(line):
        parts = line.strip().split(",")
        return Employee(parts[0], parts[1], parts[2], parts[3])

class EmployeeManager:
    def __init__(self, filename="employees.txt"):
        self.filename = filename

    def add_employee(self, employee):
        if self.search_employee(employee.employee_id, silent=True):
            print("❌ Employee ID already exists.")
            return
        with open(self.filename, "a") as file:
            file.write(employee.to_line())
        print("✅ Employee added successfully!")

    def view_all_employees(self, sort_by=None):
        try:
            with open(self.filename, "r") as file:
                lines = file.readlines()
                if not lines:
                    print("⚠️ No employee records found.")
                else:
                    employees = [Employee.from_line(line) for line in lines]
                    if sort_by == "salary":
                        employees.sort(key=lambda e: e.salary)
                    elif sort_by == "name":
                        employees.sort(key=lambda e: e.name)
                    print("📋 Employee Records:")
                    for emp in employees:
                        print(emp)
        except FileNotFoundError:
            print("❌ File not found.")

    def search_employee(self, employee_id, silent=False):
        try:
            with open(self.filename, "r") as file:
                for line in file:
                    employee = Employee.from_line(line)
                    if employee.employee_id == employee_id:
                        if not silent:
                            print("✅ Employee Found:")
                            print(employee)
                        return employee
        except FileNotFoundError:
            if not silent:
                print("❌ File not found.")
            return None
        if not silent:
            print("⚠️ Employee not found.")
        return None

    def update_employee(self, employee_id, name=None, position=None, salary=None):
        updated = False
        employees = []
        try:
            with open(self.filename, "r") as file:
                for line in file:
                    emp = Employee.from_line(line)
                    if emp.employee_id == employee_id:
                        if name:
                            emp.name = name
                        if position:
                            emp.position = position
                        if salary:
                            emp.salary = float(salary)
                        updated = True
                    employees.append(emp)
            if updated:
                with open(self.filename, "w") as file:
                    for emp in employees:
                        file.write(emp.to_line())
                print("✅ Employee updated.")
            else:
                print("❌ Employee not found.")
        except FileNotFoundError:
            print("❌ File not found.")

    def delete_employee(self, employee_id):
        deleted = False
        employees = []
        try:
            with open(self.filename, "r") as file:
                for line in file:
                    emp = Employee.from_line(line)
                    if emp.employee_id != employee_id:
                        employees.append(emp)
                    else:
                        deleted = True
            with open(self.filename, "w") as file:
                for emp in employees:
                    file.write(emp.to_line())
            if deleted:
                print("✅ Employee deleted.")
            else:
                print("❌ Employee not found.")
        except FileNotFoundError:
            print("❌ File not found.")

    def menu(self):
        while True:
            print("\nWelcome to the Employee Records Manager!")
            print("1. Add new employee record")
            print("2. View all employee records")
            print("3. Search for an employee by Employee ID")
            print("4. Update an employee's information")
            print("5. Delete an employee record")
            print("6. Sort employees by salary")
            print("7. Sort employees by name")
            print("8. Exit")
            choice = input("Enter your choice: ")
            if choice == "1":
                emp_id = input("Enter Employee ID: ")
                name = input("Enter Name: ")
                position = input("Enter Position: ")
                salary = input("Enter Salary: ")
                employee = Employee(emp_id, name, position, salary)
                self.add_employee(employee)
            elif choice == "2":
                self.view_all_employees()
            elif choice == "3":
                emp_id = input("Enter Employee ID to search: ")
                self.search_employee(emp_id)
            elif choice == "4":
                emp_id = input("Enter Employee ID to update: ")
                name = input("Enter new name (leave blank to skip): ")
                position = input("Enter new position (leave blank to skip): ")
                salary = input("Enter new salary (leave blank to skip): ")
                self.update_employee(emp_id, name or None, position or None, salary or None)
            elif choice == "5":
                emp_id = input("Enter Employee ID to delete: ")
                self.delete_employee(emp_id)
            elif choice == "6":
                self.view_all_employees(sort_by="salary")
            elif choice == "7":
                self.view_all_employees(sort_by="name")
            elif choice == "8":
                print("👋 Goodbye!")
                break
            else:
                print("❗️ Invalid choice. Please try again.")

# =========================
# task 3: To-Do Application (Flexible Storage)
# =========================
import json
import csv

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

# =========================
# Main menu for all tasks
# =========================
def main():
    while True:
        print("\nSelect a task to run:")
        print("1. Vector operations")
        print("2. Employee Records Manager")
        print("3. To-Do Application")
        print("4. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            print("Vector example usage:")
            v1 = Vector(1, 2, 3)
            v2 = Vector(4, 5, 6)
            print("v1:", v1)
            print("v2:", v2)
            print("v1 + v2:", v1 + v2)
            print("v2 - v1:", v2 - v1)
            print("v1 * v2 (dot product):", v1 * v2)
            print("3 * v1:", 3 * v1)
            print("v1 magnitude:", v1.magnitude())
            print("v1 normalized:", v1.normalize())
        elif choice == "2":
            manager = EmployeeManager()
            manager.menu()
        elif choice == "3":
            app = ToDoApp(JSONTaskStorage())
            app.main_menu()
        elif choice == "4":
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
