##Task 1
import sqlite3

conn = sqlite3.connect('lesson-11/homework/roster.db')
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS Roster (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        Name STRING,
        Species TEXT,
        AGE INTEGER
        )
''')
conn.commit()

cursor.executemany('''
    INSERT INTO Roster (name, Species, AGE)
    VALUES (?, ?, ?)
''', [
    ('Benjamin Sisko', 'Human', 40),
    ('Jadzia Dax', 'Trill', 300),
    ('Kira Nerys', 'Bajoran', 29)
])

conn.commit()

cursor.execute('''
    UPDATE Roster SET name = ? WHERE name = ?
''', ('Ezri Dax', 'Jadzia Dax'))
conn.commit()

cursor.execute('''
    SELECT * FROM Roster WHERE Species = ?         
''', ('Bajoran',))

res = cursor.fetchall()
for i in res:
    print(i[1], i[3])

cursor.execute('DELETE FROM Roster WHERE Age > ?', (100,))
conn.commit()
    
cursor.execute('ALTER TABLE Roster ADD COLUMN rank TEXT')
conn.commit()

cursor.execute("UPDATE Roster SET rank = ? WHERE name = ?", ('Captain', 'Benjamin Sisko'))
cursor.execute("UPDATE Roster SET rank = ? WHERE name = ?", ('Major', 'Kira Nerys'))
cursor.execute("UPDATE Roster SET rank = ? WHERE name = ?", ('Lieutenant', 'Ezri Dax'))
conn.commit()

cursor.execute('SELECT * FROM Roster ORDER BY AGE DESC')
rows = cursor.fetchall()
for row in rows:
    print(row[1])
    
    
##Task 2
import sqlite3

conn = sqlite3.connect('lesson-11/homework/library.db')
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS Books (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        Title STRING,
        Author TEXT,
        AGE INTEGER,
        Year_Published INTEGER,
        Genre TEXT
        )
''')
conn.commit()

cursor.executemany('''
    INSERT INTO Books (Title, Author, Year_Published, Genre)
    VALUES (?, ?, ?, ?)
''', [
    ('To Kill a Mockingbird', 'Harper Lee', 1960, 'Fiction'),
    ('1984', 'George Orwell', 1949, 'Dystopian'),
    ('The Great Gatsby', 'F. Scott Fitzgerald', 1925, 'Classic')
])

conn.commit()

cursor.execute('''
    UPDATE Books SET Year_Published = ? WHERE Year_Published = ?
''', (1984, 1950))
conn.commit()

cursor.execute('''
    SELECT * FROM Books WHERE Genre = ?         
''', ('Dystopian',))

res = cursor.fetchall()
for i in res:
    print(i[1], i[2])

cursor.execute('DELETE FROM Books WHERE Year_Published > ?', (1950,))
conn.commit()


cursor.execute('ALTER TABLE Books ADD COLUMN Rating TEXT')
conn.commit()

cursor.execute("UPDATE Books SET Rating = ? WHERE Title = ?", (4.8, 'To Kill a Mockingbird'))
cursor.execute("UPDATE Books SET Rating = ? WHERE Title = ?", (4.7, '1984'))
cursor.execute("UPDATE Books SET Rating = ? WHERE Title = ?", (4.5, 'The Great Gatsby'))
conn.commit()

cursor.execute('SELECT * FROM Books ORDER BY Year_Published ASC')
rows = cursor.fetchall()
for row in rows:
    print(row[1])