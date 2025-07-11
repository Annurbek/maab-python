# Task 1
from bs4 import BeautifulSoup

with open("weather.html", "r", encoding="utf-8") as file:
    soup = BeautifulSoup(file, 'html.parser')

max_temp = float('-inf')
max_day = ""
temperatures = []

print("📅 Прогноз погоды:\n")

for row in soup.select('tbody tr'):
    cols = [td.get_text(strip=True) for td in row.find_all('td')]
    if len(cols) != 3:
        continue

    day, temp_str, condition = cols
    try:
        temp = int(temp_str.replace('°C', ''))
    except ValueError:
        continue

    temperatures.append(temp)
    print(f"{day}: {temp}°C, {condition}")

    if temp > max_temp:
        max_temp = temp
        max_day = day

if temperatures:
    avg_temp = sum(temperatures) / len(temperatures)
    print(f"\n🌡️ Самая высокая температура: {max_temp}°C ({max_day})")
    print(f"📊 Средняя температура: {avg_temp:.1f}°C")
else:
    print("Нет доступных данных о температуре.")

# Task 2
import requests
from bs4 import BeautifulSoup
import sqlite3
import csv
from datetime import datetime

conn = sqlite3.connect('vacancys.db')
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS jobs (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT,
        company TEXT,
        location TEXT,
        description TEXT,
        link TEXT,
        updated_at TEXT,
        UNIQUE(title, company, location)
    );
''')
conn.commit()

url = "https://realpython.github.io/fake-jobs/"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")
vacancys = soup.find_all("div", class_="card-content")

for vacancy in vacancys:
    title = vacancy.find("h2", class_="title is-5").get_text(strip=True)
    company = vacancy.find("h3", class_="subtitle is-6 company").get_text(strip=True)
    location = vacancy.find("p", class_="location").get_text(strip=True)

    links = vacancy.find_all("a", class_="card-footer-item")
    link = links[1].get("href") if len(links) >= 2 else None

    if link:
        try:
            job_response = requests.get(link)
            job_soup = BeautifulSoup(job_response.text, "html.parser")
            paragraph = job_soup.find("p", class_=False)
            description = paragraph.get_text(strip=True) if paragraph else "Нет описания"
        except Exception:
            description = "Ошибка загрузки описания"
    else:
        description = "Нет ссылки"

    updated_at = datetime.now().isoformat()

    cursor.execute('''
        SELECT description, link FROM jobs
        WHERE title = ? AND company = ? AND location = ?
    ''', (title, company, location))

    existing = cursor.fetchone()

    if existing:
        old_description, old_link = existing
        if old_description != description or old_link != link:
            cursor.execute('''
                UPDATE jobs
                SET description = ?, link = ?, updated_at = ?
                WHERE title = ? AND company = ? AND location = ?
            ''', (description, link, updated_at, title, company, location))
    else:
        cursor.execute('''
            INSERT INTO jobs (title, company, location, description, link, updated_at)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', (title, company, location, description, link, updated_at))

    conn.commit()

def get_locations():
    cursor.execute("SELECT DISTINCT location FROM jobs")
    return [row[0] for row in cursor.fetchall()]

def get_companies():
    cursor.execute("SELECT DISTINCT company FROM jobs")
    return [row[0] for row in cursor.fetchall()]

def filter_by_location(location):
    cursor.execute("""
        SELECT title, company, location, description, link FROM jobs
        WHERE location = ?
    """, (location,))
    return cursor.fetchall()

def filter_by_company(company):
    cursor.execute("""
        SELECT title, company, location, description, link FROM jobs
        WHERE company = ?
    """, (company,))
    return cursor.fetchall()

def export_to_csv(filename="vacancies_export.csv"):
    cursor.execute("SELECT title, company, location, description, link FROM jobs")
    rows = cursor.fetchall()

    with open(filename, mode="w", encoding="utf-8", newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Title", "Company", "Location", "Description", "Link"])
        writer.writerows(rows)

    print(f"\n✅ Данные экспортированы в {filename}")

if __name__ == "__main__":
    print("\n🔍 ФИЛЬТРАЦИЯ ВАКАНСИЙ 🔍")
    find_arg = input("Выберите тип фильтра (1: по локации, 2: по названию компании, 3: экспорт в CSV): ")

    if find_arg == "1":
        locations = get_locations()
        print("Локации:")
        for loc in locations:
            print("-", loc)
        argument = input("Введите локацию: ")
        results = filter_by_location(argument)

    elif find_arg == "2":
        companies = get_companies()
        print("Компании:")
        for comp in companies:
            print("-", comp)
        argument = input("Введите компанию: ")
        results = filter_by_company(argument)

    elif find_arg == "3":
        export_to_csv()
        results = []

    else:
        print("Неверный выбор.")
        results = []

    if results:
        print("\n🎯 Результаты:\n")
        for job in results:
            print(f"Название: {job[0]}")
            print(f"Компания: {job[1]}")
            print(f"Локация: {job[2]}")
            print(f"Описание: {job[3]}")
            print(f"Ссылка: {job[4]}")
            print("-" * 40)
    else:
        if find_arg != "3":
            print("Нет подходящих вакансий.")

#Task 3

import requests
import json

def get_products_by_category(category: str):
    url = "https://api.demoblaze.com/bycat"
    headers = {"Content-Type": "application/json"}
    payload = json.dumps({"cat": category})

    try:
        response = requests.post(url, headers=headers, data=payload, timeout=10)
        response.raise_for_status()
        return response.json().get("Items", [])
    except requests.RequestException as e:
        print(f"Ошибка API: {e}")
        return []

all_data = {}
categories = ["phone", "notebook", "monitor"]

for category in categories:
    items = get_products_by_category(category)
    filtered = [{
        "title": p.get("title"),
        "price": p.get("price"),
        "description": p.get("desc"),
        "image": p.get("img"),
        "category": category
    } for p in items]
    all_data[category] = filtered
    print(f"✅ {category}: {len(filtered)} товаров")

with open("products_all.json", "w", encoding="utf-8") as f:
    json.dump(all_data, f, ensure_ascii=False, indent=4)

print("\n📁 Данные сохранены в products_all.json")