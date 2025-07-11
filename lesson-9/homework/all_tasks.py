### Task 1
class BookNotFoundException(Exception):
    def __init__(self, title):
        self.title = title
        super().__init__(f"Book '{self.title}' not found in library.")

class BookAlreadyBorrowedException(Exception):
    def __init__(self, title):
        self.title = title
        super().__init__(f"Book '{self.title}' is already borrowed.")

class MemberLimitExceededException(Exception):
    def __init__(self, name, limit):
        self.name = name
        self.limit = limit
        super().__init__(f"Member '{self.name}' cannot borrow more than {self.limit} books.")


class Books:
    def __init__(self, title, author, is_borrowed=False):
        self.title = title
        self.author = author
        self.is_borrowed = is_borrowed
    

    def __str__(self):
        return f"'{self.title}' by {self.author}"

class Library:
    def __init__(self):
        self.books = []
        self.members = []

    def add_book(self, book):
        self.books.append(book)
        return f"Book {book} added to library."

    def find_book(self, title):
        for book in self.books:
            if book.title == title:
                return book
        raise BookNotFoundException(title)
    
    def add_member(self, member):
        self.members.append(member)
        return f"Member '{member.name}' registered."

    def list_books(self):
        return [str(book) for book in self.books]

    def list_members(self):
        return [member.name for member in self.members]

class Member:
    def __init__(self, name, books_borrowed=None):
        self.name = name
        self.books_borrowed = books_borrowed if books_borrowed is not None else []

    def borrow_book(self, book):
        if len(self.books_borrowed) >= 3:
            raise MemberLimitExceededException(self.name, 3)
        if book.is_borrowed:
            raise BookAlreadyBorrowedException(book.title)
        
        book.is_borrowed = True
        self.books_borrowed.append(book)
        return f"{self.name} borrowed '{book.title}'"

    def return_book(self, book):
        if book in self.books_borrowed:
            book.is_borrowed = False
            self.books_borrowed.remove(book)
            return f"{self.name} returned '{book.title}'"
        else:
            return f"{self.name} does not have '{book.title}' borrowed"
    
if __name__ == "__main__":
    library = Library()

    book1 = Books("1984", "George Orwell")
    book2 = Books("To Kill a Mockingbird", "Harper Lee")
    print(library.add_book(book1))
    print(library.add_book(book2))

    member1 = Member("Alice")
    member2 = Member("Bob")
    print(library.add_member(member1))
    print(library.add_member(member2))

    try:
        print(member1.borrow_book(book1))
    except Exception as e:
        print("⚠️", e)

    try:
        print(member2.borrow_book(book1))
    except BookAlreadyBorrowedException as e:
        print("✅ Exception caught:", e)

    print(member1.return_book(book1))

    try:
        print(member2.borrow_book(book1))
    except Exception as e:
        print("⚠️", e)

    book3 = Books("Book Three", "Author A")
    book4 = Books("Book Four", "Author B")
    book5 = Books("Book Five", "Author C")
    library.add_book(book3)
    library.add_book(book4)
    library.add_book(book5)

    try:
        print(member2.borrow_book(book3))
        print(member2.borrow_book(book4))
        print(member2.borrow_book(book5))
    except MemberLimitExceededException as e:
        print("✅ Exception caught:", e)

    try:
        library.find_book("Nonexistent Book")
    except BookNotFoundException as e:
        print("✅ Exception caught:", e)

# Task 2
import csv
from collections import defaultdict

grades = []
subject_totals = defaultdict(float)
subject_counts = defaultdict(int)

with open('grades.csv', 'r', newline='') as file:
    reader = csv.reader(file)
    for row in reader:
        student = {
            'ismi': row[0],
            'fan': row[1],
            'daraja': float(row[2])
        }
        grades.append(student)

for record in grades:
    subject = record['fan']
    grade = record['daraja']
    subject_totals[subject] += grade
    subject_counts[subject] += 1

for subject in subject_totals:
    avg = subject_totals[subject] / subject_counts[subject]
    print(f"{subject}: o'rtacha ball = {avg:.2f}")

## Task 3
import json
import csv

def load_tasks(filename='tasks.json'):
    with open(filename, 'r', encoding='utf-8') as file:
        tasks = json.load(file)
    return tasks

def save_tasks(tasks, filename='tasks.json'):
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(tasks, file, ensure_ascii=False, indent=4)

def display_tasks(tasks):
    print("ID | Vazifa                       | Tugallangan | Prioritet")
    print("---|-----------------------------|-------------|-----------")
    for task in tasks:
        tugallangan = "Ha" if task.get("tugallangan", False) else "Yo'q"
        print(f"{task['id']:2} | {task['vazifa'][:27]:27} | {tugallangan:11} | {task['prioritet']}")

def task_statistics(tasks):
    jami = len(tasks)
    bajarilgan = sum(1 for t in tasks if t.get("tugallangan"))
    kutilayotgan = jami - bajarilgan
    ortacha_prioritet = sum(t["prioritet"] for t in tasks) / jami if jami else 0

    print("\n📊 Statistikalar:")
    print(f"Jami vazifalar      : {jami}")
    print(f"Bajarilgan vazifalar: {bajarilgan}")
    print(f"Kutilayotgan vazifalar: {kutilayotgan}")
    print(f"O'rtacha ustuvorlik : {ortacha_prioritet:.2f}")

def convert_to_csv(tasks, filename='tasks.csv'):
    with open(filename, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(["ID", "Vazifa", "Bajarildi", "Ustuvorlik"])
        for t in tasks:
            writer.writerow([
                t['id'],
                t['vazifa'],
                "to'g'ri" if t.get("tugallangan") else "noto'g'ri",
                t['prioritet']
            ])
    print(f"\n✅ CSV fayli '{filename}' ga saqlandi.")

if __name__ == "__main__":
    tasks = load_tasks()
    display_tasks(tasks)
    task_statistics(tasks)
    convert_to_csv(tasks)
