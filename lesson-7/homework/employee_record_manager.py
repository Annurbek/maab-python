#employee record manager
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

if __name__ == "__main__":
    manager = EmployeeManager()
    manager.menu()
    manager.menu()
