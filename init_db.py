import sqlite3

connection = sqlite3.connect('database')


with open('tables.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

cur.execute("INSERT INTO users (name, email) VALUES (?, ?)",
            ('Kiss Geza', 'kgeza85@valami.com')
            )

connection.commit()
connection.close()