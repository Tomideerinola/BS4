import requests
from bs4 import BeautifulSoup
import sqlite3

# 1️⃣ Connect / create database
conn = sqlite3.connect("jobs.db")
cursor = conn.cursor()

# 2️⃣ Create table
cursor.execute("""
CREATE TABLE IF NOT EXISTS jobs (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT,
    company TEXT,
    location TEXT,
    link TEXT
)
""")
conn.commit()

# 3️⃣ Scrape job listings
url = "https://realpython.github.io/fake-jobs/"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")
job_cards = soup.find_all("div", class_="card-content")

for job in job_cards:
    title = job.find("h2", class_="title").text.strip()
    company = job.find("h3", class_="company").text.strip()
    location = job.find("p", class_="location").text.strip()
    link = job.find("a")["href"]

    # 4️⃣ Insert into database
    cursor.execute(
        "INSERT INTO jobs (title, company, location, link) VALUES (?, ?, ?, ?)",
        (title, company, location, link)
    )

# 5️⃣ Commit and close
conn.commit()
conn.close()

print("Jobs scraping complete! Saved to jobs.db")
