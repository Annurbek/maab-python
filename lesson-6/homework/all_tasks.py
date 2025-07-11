# task 1: Zero Check Decorator
def check(func):
    def wrapper(a, b):
        if b == 0:
            return "Denominator can't be zero"
        return func(a, b)
    return wrapper

@check
def div(a, b):
    return a / b

# Пример использования:
# print(div(6, 2))  # 3.0
# print(div(6, 0))  # "Denominator can't be zero"

# task 2: Employee Records Manager
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
    try:
        with open("employees.txt", "r") as file:
            for record in file:
                if record.startswith(emp_id + ","):
                    print("Employee Found:", record.strip(), "\n")
                    return
        print("Employee not found.\n")
    except FileNotFoundError:
        print("No employee records found.\n")

def update_employee():
    emp_id = input("Enter Employee ID to update: ")
    records = []
    found = False
    try:
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
    except FileNotFoundError:
        print("No employee records found.\n")

def delete_employee():
    emp_id = input("Enter Employee ID to delete: ")
    records = []
    found = False
    try:
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
    except FileNotFoundError:
        print("No employee records found.\n")

def employee_manager_menu():
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

# task 3: Word Frequency Counter
import string
from collections import Counter

def get_text():
    if not os.path.exists("sample.txt"):
        print("sample.txt does not exist. Please enter text to create it.")
        text = input("Enter your paragraph: ")
        with open("sample.txt", "w") as file:
            file.write(text)
    with open("sample.txt", "r") as file:
        return file.read()

def clean_text(text):
    text = text.lower()
    text = text.translate(str.maketrans('', '', string.punctuation))
    words = text.split()
    return words

def count_words(words):
    return Counter(words)

def display_results(word_counts, top_n=5):
    total_words = sum(word_counts.values())
    print(f"Total words: {total_words}")
    print("Top", top_n, "most common words:")
    for word, count in word_counts.most_common(top_n):
        print(f"{word} - {count} times")

def save_results(word_counts, total_words, top_n=5):
    with open("word_count_report.txt", "w") as file:
        file.write("Word Count Report\n")
        file.write(f"Total Words: {total_words}\n")
        file.write(f"Top {top_n} Words:\n")
        for word, count in word_counts.most_common(top_n):
            file.write(f"{word} - {count}\n")
    print("Results saved to word_count_report.txt")

def word_frequency_counter():
    text = get_text()
    words = clean_text(text)
    word_counts = count_words(words)
    total_words = sum(word_counts.values())
    try:
        top_n = int(input("Enter the number of top common words to display: "))
    except ValueError:
        top_n = 5
    display_results(word_counts, top_n)
    save_results(word_counts, total_words, top_n)

# task 4: Main menu to select task
def main():
    while True:
        print("\nSelect a task to run:")
        print("1. Zero Check Decorator")
        print("2. Employee Records Manager")
        print("3. Word Frequency Counter")
        print("4. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            try:
                a = float(input("Enter numerator: "))
                b = float(input("Enter denominator: "))
                print(div(a, b))
            except ValueError:
                print("Invalid input.")
        elif choice == "2":
            employee_manager_menu()
        elif choice == "3":
            word_frequency_counter()
        elif choice == "4":
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please try again.\n")

if __name__ == "__main__":
    main()
