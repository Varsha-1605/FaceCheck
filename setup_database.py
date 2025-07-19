import sqlite3

# Connect to the SQLite database (it will be created if it doesn't exist)
conn = sqlite3.connect('attendance.db')
cursor = conn.cursor()

# Create a table for students if it doesn't already exist
cursor.execute('''
CREATE TABLE IF NOT EXISTS students (
    id TEXT PRIMARY KEY,
    name TEXT NOT NULL,
    major TEXT NOT NULL,
    starting_year INTEGER,
    total_attendance INTEGER,
    standing TEXT,
    year INTEGER,
    last_attendance_time TEXT
)
''')

# Data to be inserted
data = {
    "123456": {
        "name": "Varsha Dewangan",
        "major": "AIML",
        "starting_year": 2022,
        "total_attendance": 10,
        "standing": "A",
        "year": 4,
        "last_attendance_time": "2025-05-20 13:00:00"
    },
    "234567": {
        "name": "Sundar Pichai",
        "major": "Data Science",
        "starting_year": 2020,
        "total_attendance": 12,
        "standing": "B",
        "year": 5,
        "last_attendance_time": "2025-06-10 09:30:00"
    },
    "345678": {
        "name": "Elon Musk",
        "major": "Aerospace AI",
        "starting_year": 2019,
        "total_attendance": 15,
        "standing": "S",
        "year": 6,
        "last_attendance_time": "2025-07-01 17:45:00"
    }
}

# Insert data into the table
for key, value in data.items():
    cursor.execute('''
    INSERT OR REPLACE INTO students (id, name, major, starting_year, total_attendance, standing, year, last_attendance_time)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    ''', (key, value['name'], value['major'], value['starting_year'], value['total_attendance'], value['standing'], value['year'], value['last_attendance_time']))

# Commit the changes and close the connection
conn.commit()
conn.close()

print("Database setup complete. 'attendance.db' is ready.")