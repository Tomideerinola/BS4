import sqlite3

conn = sqlite3.connect("joby.db")
cursor = conn.cursor()

cursor.execute("SELECT title, company, location FROM jobs")
rows = cursor.fetchall()

for row in rows:
    print(row)

cursor.close()
conn.close()
