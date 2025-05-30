class Employee:
    """Класс для представления сотрудника с основными атрибутами и методами."""
    
    def __init__(self, employee_id, name, position, salary):
        """
        Инициализация нового сотрудника.
        
        Args:
            employee_id: Уникальный идентификатор сотрудника
            name: Имя сотрудника
            position: Должность сотрудника
            salary: Зарплата сотрудника
        """
        self.employee_id = employee_id
        self.name = name
        self.position = position
        try:
            self.salary = float(salary)
        except ValueError:
            raise ValueError("Зарплата должна быть числом")

    def __str__(self):
        return f"{self.employee_id}, {self.name}, {self.position}, {self.salary:.2f}"

    def to_line(self):
        return f"{self.employee_id},{self.name},{self.position},{self.salary}\n"

    @staticmethod
    def from_line(line):
        """Создает объект Employee из строки файла."""
        try:
            parts = line.strip().split(",")
            if len(parts) != 4:
                raise ValueError("Неверный формат записи")
            return Employee(parts[0], parts[1], parts[2], parts[3])
        except Exception as e:
            raise ValueError(f"Ошибка при чтении записи: {str(e)}")
    
class EmployeeManager:
    """Класс для управления записями сотрудников."""

    def __init__(self, filename="employees.txt"):
        self.filename = filename
    
    def validate_employee_id(self, employee_id):
        """Проверяет корректность ID сотрудника."""
        if not employee_id.strip():
            raise ValueError("ID сотрудника не может быть пустым")
        if not employee_id.isalnum():
            raise ValueError("ID сотрудника должен содержать только буквы и цифры")
        return True

    def add_employee(self, employee):
        """Добавляет нового сотрудника в файл."""
        try:
            self.validate_employee_id(employee.employee_id)
            if self.search_employee(employee.employee_id):
                print("❌ Сотрудник с таким ID уже существует.")
                return False
            with open(self.filename, "a") as file:
                file.write(employee.to_line())
            print("✅ Сотрудник успешно добавлен!")
            return True
        except Exception as e:
            print(f"❌ Ошибка при добавлении сотрудника: {str(e)}")
            return False

    def view_all_employees(self, sort_by=None):
        """
        Просмотр всех сотрудников с опциональной сортировкой.
        
        Args:
            sort_by: Поле для сортировки ('name', 'salary', 'position')
        """
        try:
            employees = []
            with open(self.filename, "r") as file:
                for line in file:
                    try:
                        employees.append(Employee.from_line(line))
                    except ValueError as e:
                        print(f"⚠️ Пропущена некорректная запись: {str(e)}")
                        continue

            if not employees:
                print("⚠️ Записи о сотрудниках не найдены.")
                return

            if sort_by:
                if sort_by == 'name':
                    employees.sort(key=lambda x: x.name)
                elif sort_by == 'salary':
                    employees.sort(key=lambda x: x.salary)
                elif sort_by == 'position':
                    employees.sort(key=lambda x: x.position)

            print("\n📋 Записи о сотрудниках:")
            for emp in employees:
                print(emp)
        except FileNotFoundError:
            print("❌ Файл не найден.")
        except Exception as e:
            print(f"❌ Ошибка при чтении файла: {str(e)}")

    def search_employee(self, employee_id):
        """Поиск сотрудника по ID."""
        try:
            with open(self.filename, "r") as file:
                for line in file:
                    try:
                        employee = Employee.from_line(line)
                        if employee.employee_id == employee_id:
                            return employee
                    except ValueError:
                        continue
        except FileNotFoundError:
            print("❌ Файл не найден.")
        return None

    def update_employee(self, employee_id, name=None, position=None, salary=None):
        """Обновление информации о сотруднике."""
        updated = False
        employees = []

        try:
            with open(self.filename, "r") as file:
                for line in file:
                    try:
                        emp = Employee.from_line(line)
                        if emp.employee_id == employee_id:
                            if name and name.strip():
                                emp.name = name
                            if position and position.strip():
                                emp.position = position
                            if salary and salary.strip():
                                emp.salary = float(salary)
                            updated = True
                        employees.append(emp)
                    except ValueError as e:
                        print(f"⚠️ Пропущена некорректная запись: {str(e)}")
                        continue

            if updated:
                with open(self.filename, "w") as file:
                    for emp in employees:
                        file.write(emp.to_line())
                print("✅ Информация о сотруднике обновлена.")
            else:
                print("❌ Сотрудник не найден.")
        except FileNotFoundError:
            print("❌ Файл не найден.")
        except Exception as e:
            print(f"❌ Ошибка при обновлении: {str(e)}")

    def delete_employee(self, employee_id):
        """Удаление записи о сотруднике."""
        deleted = False
        employees = []

        try:
            with open(self.filename, "r") as file:
                for line in file:
                    try:
                        emp = Employee.from_line(line)
                        if emp.employee_id != employee_id:
                            employees.append(emp)
                        else:
                            deleted = True
                    except ValueError:
                        continue

            with open(self.filename, "w") as file:
                for emp in employees:
                    file.write(emp.to_line())

            if deleted:
                print("✅ Сотрудник удален.")
            else:
                print("❌ Сотрудник не найден.")
        except FileNotFoundError:
            print("❌ Файл не найден.")
        except Exception as e:
            print(f"❌ Ошибка при удалении: {str(e)}")

    def menu(self):
        while True:
            print("\nДобро пожаловать в диспетчер записей сотрудников!")
            print("1. Добавить новую запись сотрудника")
            print("2. Просмотреть все записи сотрудников")
            print("3. Поиск сотрудника по идентификатору сотрудника")
            print("4. Обновить информацию о сотруднике")
            print("5. Удалить запись сотрудника")
            print("6. Выйти")

            choice = input("Введите свой выбор: ")

            if choice == "1":
                try:
                    emp_id = input("Введите идентификационный номер сотрудника: ")
                    name = input("Введите имя: ")
                    position = input("Введите должность: ")
                    salary = input("Введите зарплату: ")
                    employee = Employee(emp_id, name, position, salary)
                    self.add_employee(employee)
                except ValueError as e:
                    print(f"❌ Ошибка: {str(e)}")

            elif choice == "2":
                print("\nКак вы хотите отсортировать записи?")
                print("1. По имени")
                print("2. По зарплате")
                print("3. По должности")
                print("4. Без сортировки")
                sort_choice = input("Введите свой выбор (1-4): ")
                
                sort_by = None
                if sort_choice == "1":
                    sort_by = "name"
                elif sort_choice == "2":
                    sort_by = "salary"
                elif sort_choice == "3":
                    sort_by = "position"
                
                self.view_all_employees(sort_by)

            elif choice == "3":
                emp_id = input("Введите идентификационный номер сотрудника для поиска: ")
                employee = self.search_employee(emp_id)
                if employee:
                    print("✅ Сотрудник найден:")
                    print(employee)
                else:
                    print("❌ Сотрудник не найден.")

            elif choice == "4":
                emp_id = input("Введите идентификационный номер сотрудника для обновления: ")
                name = input("Введите новое имя (оставьте пустым, чтобы пропустить): ")
                position = input("Введите новую должность (оставьте пустым, чтобы пропустить): ")
                salary = input("Введите новую зарплату (оставьте пустым, чтобы пропустить): ")
                self.update_employee(emp_id, name, position, salary)

            elif choice == "5":
                emp_id = input("Введите идентификационный номер сотрудника для удаления: ")
                self.delete_employee(emp_id)

            elif choice == "6":
                print("👋 До свидания!")
                break
            else:
                print("❗ Неверный выбор. Пожалуйста, попробуйте снова.")

if __name__ == "__main__":
    manager = EmployeeManager()
    manager.menu()