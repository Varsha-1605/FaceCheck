<div align="center">
<img src="https://www.google.com/search?q=https://placehold.co/1200x400/2c3e50/FFFFFF%3Ftext%3DFaceCheck%26font%3Draleway" alt="FaceCheck Banner">
<h1>FaceCheck: Real-Time Web-Based Attendance System</h1>
<p>
A modern, real-time attendance system that uses facial recognition through a simple web interface.
</p>

<!-- Badges -->

<p>
<img src="https://www.google.com/search?q=https://img.shields.io/badge/Python-3.8%2B-blue.svg" alt="Python Version">
<img src="https://www.google.com/search?q=https://img.shields.io/badge/Framework-Flask-green.svg" alt="Flask Framework">
<img src="https://www.google.com/search?q=https://img.shields.io/badge/License-MIT-yellow.svg" alt="License">
<img src="https://www.google.com/search?q=https://img.shields.io/badge/status-active-brightgreen" alt="Project Status">
</p>
</div>

FaceCheck leverages your webcam to create a seamless and efficient attendance-taking process, eliminating the need for manual check-ins. Built with Python and Flask, it's designed to be simple, scalable, and run entirely on your local machine.

📸 Demo
<div align="center">
<!-- TODO: Add a GIF of the application in action -->
<img src="https://www.google.com/search?q=https://placehold.co/600x400/ecf0f1/95a5a6%3Ftext%3DApp%2BDemo%2BGIF" alt="Application Demo">
<p><em>A brief demonstration of the face recognition and attendance marking process.</em></p>
</div>

✨ Key Features
🚀 Real-Time Recognition: Instantly detects and identifies registered students from a live webcam feed.

🌐 Web-Based Interface: Accessible from any modern browser on your local network. No desktop app needed.

🔒 Local Data Storage: Ensures privacy and offline functionality by storing all data locally using SQLite.

💡 Dynamic Feedback: The UI provides immediate visual confirmation for marked attendance, duplicates, or unknown faces.

⏱️ Cooldown Period: Prevents accidental duplicate entries with a timed cooldown after a successful check-in.

🌱 Scalable & Simple: Easily add new students by adding their image and re-running a single script.

🛠️ Technology Stack
Category

Technologies

Backend

Python, Flask, Flask-SocketIO

Face Engine

face_recognition, opencv-python, Pillow

Database

SQLite

Frontend

HTML5, CSS3, JavaScript

Data Handling

pickle, Base64

DevOps

Git, Virtual Environments

🚀 Getting Started
Follow these instructions to set up and run the project on your local machine.

1. Prerequisites
Python 3.8+

Git

A webcam

2. Installation
Clone the repository:

git clone [https://github.com/your-username/FaceCheck.git](https://github.com/your-username/FaceCheck.git)
cd FaceCheck

Create and activate a virtual environment:

# Create the environment
python -m venv venv

# Activate it
# Windows
venv\Scripts\activate
# macOS / Linux
source venv/bin/activate

Install the required dependencies:
First, create a requirements.txt file with the following content:

Flask
Flask-SocketIO
numpy
opencv-python
face_recognition
Pillow

Then, run the installation command:

pip install -r requirements.txt

3. System Setup
Add Student Images:
Place images of students in the images/ directory. The filename for each image must be the student's unique ID (e.g., 123456.jpg).

Run the Setup Scripts:
Execute these scripts in order to populate the database and generate the face encodings.

# 1. Create the database and add student records
python setup_database.py

# 2. Generate and save face encodings from the images
python EncoderGenerator.py

4. Launch the Application
Start the Flask web server with this command:

python app.py

Once the server is running, open your browser and navigate to http://127.0.0.1:5000.

📂 Project Structure
/FaceCheck/
├── .gitignore
├── app.py
├── EncoderGenerator.py
├── setup_database.py
├── requirements.txt
├── README.md
├── attendance.db
├── EncodeFile.p
├── images/
│   └── 123456.jpg
├── static/
│   └── script.js
└── templates/
    └── index.html

🤝 Contributing
Contributions are welcome! If you have suggestions for improvements or want to fix a bug, please feel free to:

Fork the Project

Create your Feature Branch (git checkout -b feature/AmazingFeature)

Commit your Changes (git commit -m 'Add some AmazingFeature')

Push to the Branch (git push origin feature/AmazingFeature)

Open a Pull Request

📄 License
This project is distributed under the MIT License. See the LICENSE file for more information.
