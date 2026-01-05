import sqlite3

conn = sqlite3.connect("jobs.db")
cursor = conn.cursor()

cursor.execute("""
INSERT INTO jobs (title, company, location)
VALUES (?, ?, ?)
""", ("Python Developer", "OpenAI", "Remote"))

conn.commit()
cursor.close()
conn.close()

print("Test job inserted")
