# scrape_to_db.py

import sqlite3
import requests
from bs4 import BeautifulSoup

# 1️⃣ Connect to the database (it will use the clean jobs.db)
conn = sqlite3.connect("joby.db")
cursor = conn.cursor()

# 2️⃣ Create table if it doesn't exist
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

# 3️⃣ Fetch the webpage (example: Real Python job listings)
url = "https://realpython.com/jobs/"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

# 4️⃣ Scrape job info
# Adjust these selectors based on the website you are scraping
job_cards = soup.find_all("div", class_="card")  # example container

for job in job_cards:
    title = job.find("h2").text.strip() if job.find("h2") else "N/A"
    company = job.find("p", class_="company").text.strip() if job.find("p", class_="company") else "N/A"
    location = job.find("p", class_="location").text.strip() if job.find("p", class_="location") else "N/A"
    link_tag = job.find("a", href=True)
    link = link_tag["href"] if link_tag else "N/A"

    # 5️⃣ Insert into database
    cursor.execute("""
        INSERT INTO jobs (title, company, location, link)
        VALUES (?, ?, ?, ?)
    """, (title, company, location, link))

# 6️⃣ Commit and close
conn.commit()
cursor.close()
conn.close()

print("Scraping done and saved to database!")
