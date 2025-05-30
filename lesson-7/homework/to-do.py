import json
import csv
import os
from datetime import datetime

class Tasks:
    VALID_STATUSES = ["В ожидании", "В процессе", "Завершено"]
    
    def __init__(self, task_id, task_name, task_description, date_line, status):

        self.task_id = task_id
        self.task_name = task_name
        self.task_description = task_description
        
        if date_line:
            try:
                datetime.strptime(date_line, "%Y-%m-%d")
                self.date_line = date_line
            except ValueError:
                raise ValueError("Дата должна быть в формате ГГГГ-ММ-ДД")
        else:
            self.date_line = ""
        
        if status not in self.VALID_STATUSES:
            raise ValueError(f"Недопустимый статус. Допустимые статусы: {', '.join(self.VALID_STATUSES)}")
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
        try:
            parts = line.strip().split(",")
            if len(parts) != 5:
                raise ValueError("Некорректный формат записи")
            return Tasks(parts[0], parts[1], parts[2], parts[3], parts[4])
        except Exception as e:
            raise ValueError(f"Ошибка при чтении записи: {str(e)}")

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
            print("❌ Задача с таким ID уже существует.")
            return
        self.tasks.append(task)
        self.storage.save_tasks(self.tasks)
        print("✅ Задача успешно добавлена!")
    
    def view_all_tasks(self):
        if not self.tasks:
            print("⚠️ Задачи не найдены.")
        else:
            print("📋 Список задач:")
            for task in self.tasks:
                print(task)
    
    def search_task(self, task_id):
        for task in self.tasks:
            if task.task_id == task_id:
                return task
        print("⚠️ Задача не найдена.")
        return None
    
    def update_task(self, task_id, task_name=None, task_description=None, 
                   date_line=None, status=None):
        task = self.search_task(task_id)
        if task:
            try:
                if task_name:
                    task.task_name = task_name
                if task_description:
                    task.task_description = task_description
                if date_line:
                    datetime.strptime(date_line, "%Y-%m-%d")
                    task.date_line = date_line
                if status:
                    if status not in Tasks.VALID_STATUSES:
                        raise ValueError(f"Недопустимый статус. Допустимые статусы: {', '.join(Tasks.VALID_STATUSES)}")
                    task.status = status
                self.storage.save_tasks(self.tasks)
                print("✅ Задача обновлена.")
            except ValueError as e:
                print(f"❌ Ошибка: {str(e)}")
        else:
            print("❌ Задача не найдена.")
    
    def delete_task(self, task_id):
        initial_length = len(self.tasks)
        self.tasks = [task for task in self.tasks if task.task_id != task_id]
        
        if len(self.tasks) < initial_length:
            self.storage.save_tasks(self.tasks)
            print("✅ Задача удалена.")
        else:
            print("❌ Задача не найдена.")

    def filter_by_status(self, status):
        if status not in Tasks.VALID_STATUSES:
            print(f"❌ Недопустимый статус. Допустимые статусы: {', '.join(Tasks.VALID_STATUSES)}")
            return []
            
        filtered_tasks = [task for task in self.tasks if task.status == status]
        if not filtered_tasks:
            print(f"⚠️ Задачи со статусом '{status}' не найдены")
        else:
            print(f"📋 Задачи со статусом '{status}':")
            for task in filtered_tasks:
                print(task)
        return filtered_tasks
    
    def main(self):
        while True:
            print("\nДобро пожаловать в приложение «Дела»!")
            print("1. Добавить новую задачу")
            print("2. Просмотреть все задачи")
            print("3. Обновить задачу")
            print("4. Удалить задачу")
            print("5. Фильтрация задач по статусу")
            print("6. Сохранить задачи")
            print("7. Загрузить задачи")
            print("8. Выйти")
            choice = input("Введите свой выбор: ")

            if choice == "1":
                try:
                    task_id = input("Введите ID задачи: ")
                    task_name = input("Введите название: ")
                    task_description = input("Введите описание: ")
                    date_line = input("Введите срок выполнения (ГГГГ-ММ-ДД): ")
                    print(f"Допустимые статусы: {', '.join(Tasks.VALID_STATUSES)}")
                    status = input("Введите статус: ")
                    new_task = Tasks(task_id, task_name, task_description, date_line, status)
                    self.add_task(new_task)
                except ValueError as e:
                    print(f"❌ Ошибка: {str(e)}")
            elif choice == "2":
                self.view_all_tasks()
            elif choice == "3":
                task_id = input("Введите ID задачи для обновления: ")
                task_name = input("Введите новое название (или нажмите Enter для пропуска): ")
                task_description = input("Введите новое описание (или нажмите Enter для пропуска): ")
                date_line = input("Введите новый срок (ГГГГ-ММ-ДД) (или нажмите Enter для пропуска): ")
                print(f"Допустимые статусы: {', '.join(Tasks.VALID_STATUSES)}")
                status = input("Введите новый статус (или нажмите Enter для пропуска): ")
                self.update_task(task_id, task_name or None, task_description or None,
                               date_line or None, status or None)
            elif choice == "4":
                task_id = input("Введите ID задачи для удаления: ")
                self.delete_task(task_id)
            elif choice == "5":
                print(f"Допустимые статусы: {', '.join(Tasks.VALID_STATUSES)}")
                status = input("Введите статус для фильтрации: ")
                self.filter_by_status(status)
            elif choice == "6":
                self.storage.save_tasks(self.tasks)
                print("✅ Задачи успешно сохранены!")
            elif choice == "7":
                self.tasks = self.storage.load_tasks()
                print("✅ Задачи успешно загружены!")
            elif choice == "8":
                print("👋 До свидания!")
                break
            else:
                print("❌ Неверный выбор. Пожалуйста, попробуйте снова.")

if __name__ == "__main__":
    print("Выберите формат хранения задач:")
    print("1. JSON (.json)")
    print("2. CSV (.csv)")
    print("3. Текстовый файл (.txt)")
    
    format_choice = input("Введите номер формата (1-3): ")
    
    if format_choice == "1":
        filename = "tasks.json"
    elif format_choice == "2":
        filename = "tasks.csv"
    elif format_choice == "3":
        filename = "tasks.txt"
    else:
        print("❌ Неверный выбор. Будет использован формат JSON.")
        filename = "tasks.json"
    
    storage = StorageManage(filename)
    manager = TaskManage(storage)
    manager.main()