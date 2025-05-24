#Employee Records Manager
import os

def add_employee():
    with open("employees.txt", "a") as file:
        emp_id = input("Enter Employee ID: ")
        name = input("Enter Name: ")
        position = input("Enter Position: ")
        salary = input("Enter Salary: ")
        file.write(f"{emp_id}, {name}, {position}, {salary}\n")
        print("Employee record added successfully!\n")

def view_employees():
    try:
        with open("employees.txt", "r") as file:
            records = file.readlines()
            if not records:
                print("No employee records found.\n")
            else:
                print("Employee Records:")
                for record in records:
                    print(record.strip())
                print()
    except FileNotFoundError:
        print("No employee records found.\n")

def search_employee():
    emp_id = input("Enter Employee ID to search: ")
    with open("employees.txt", "r") as file:
        for record in file:
            if record.startswith(emp_id + ","):
                print("Employee Found:", record.strip(), "\n")
                return
    print("Employee not found.\n")

def update_employee():
    emp_id = input("Enter Employee ID to update: ")
    records = []
    found = False
    with open("employees.txt", "r") as file:
        for record in file:
            if record.startswith(emp_id + ","):
                name = input("Enter New Name: ")
                position = input("Enter New Position: ")
                salary = input("Enter New Salary: ")
                records.append(f"{emp_id}, {name}, {position}, {salary}\n")
                found = True
            else:
                records.append(record)
    if found:
        with open("employees.txt", "w") as file:
            file.writelines(records)
        print("Employee record updated successfully!\n")
    else:
        print("Employee not found.\n")

def delete_employee():
    emp_id = input("Enter Employee ID to delete: ")
    records = []
    found = False
    with open("employees.txt", "r") as file:
        for record in file:
            if not record.startswith(emp_id + ","):
                records.append(record)
            else:
                found = True
    if found:
        with open("employees.txt", "w") as file:
            file.writelines(records)
        print("Employee record deleted successfully!\n")
    else:
        print("Employee not found.\n")

def main():
    while True:
        print("Employee Records Manager")
        print("1. Add new employee record")
        print("2. View all employee records")
        print("3. Search for an employee by Employee ID")
        print("4. Update an employee's information")
        print("5. Delete an employee record")
        print("6. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            add_employee()
        elif choice == "2":
            view_employees()
        elif choice == "3":
            search_employee()
        elif choice == "4":
            update_employee()
        elif choice == "5":
            delete_employee()
        elif choice == "6":
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please try again.\n")

if __name__ == "__main__":
    main()