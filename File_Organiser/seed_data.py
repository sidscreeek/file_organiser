import os
import random
import csv
import json
from datetime import datetime, timedelta

folder = "downloads"

first_names = ["Alex", "Sam", "Jordan", "Taylor", "Morgan", "Riley", "Casey", "Jamie"]
last_names = ["Smith", "Johnson", "Williams", "Brown", "Jones", "Garcia", "Miller"]
domains = ["gmail.com", "yahoo.com", "outlook.com", "test.com"]

def random_name():
    return f"{random.choice(first_names)} {random.choice(last_names)}"

def random_email(name):
    return f"{name.split()[0].lower()}{random.randint(1,999)}@{random.choice(domains)}"

def random_date():
    start = datetime(2023, 1, 1)
    return (start + timedelta(days=random.randint(0, 700))).strftime("%Y-%m-%d")

def fill_file(filepath):
    ext = os.path.splitext(filepath)[1].lower()

    if ext == ".txt":
        with open(filepath, "w") as f:
            for _ in range(5):
                f.write(f"{random_name()} - {random_date()}\n")

    elif ext == ".csv":
        with open(filepath, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["name", "email", "date"])
            for _ in range(5):
                name = random_name()
                writer.writerow([name, random_email(name), random_date()])

    elif ext == ".json":
        name = random_name()
        data = {
            "name": name,
            "email": random_email(name),
            "date": random_date(),
            "id": random.randint(1000, 9999)
        }
        with open(filepath, "w") as f:
            json.dump(data, f, indent=2)

    else:
        with open(filepath, "w") as f:
            f.write(f"Dummy content - {random_name()} - {random_date()}\n")

for filename in os.listdir(folder):
    filepath = os.path.join(folder, filename)
    if os.path.isfile(filepath):
        fill_file(filepath)

print("Files populated with dummy data.")