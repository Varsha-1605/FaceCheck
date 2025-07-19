FaceCheck: Real-Time Web-Based Attendance System
FaceCheck is a modern, real-time attendance system that uses facial recognition to mark attendance through a simple web interface. Built with Python and Flask, it leverages your webcam to create a seamless and efficient attendance-taking process, eliminating the need for manual check-ins.

✨ Features
Real-Time Face Recognition: Instantly detects and identifies registered students via a live webcam feed.

Web-Based Interface: Accessible from any modern web browser on your local network. No desktop application needed.

Local Data Storage: All student data and face encodings are stored locally using SQLite and pickle files, ensuring privacy and offline functionality.

Dynamic Feedback: The UI provides immediate visual feedback, confirming whether attendance was marked, if a student was already marked, or if a face is unknown.

Cooldown Period: Prevents accidental duplicate entries by implementing a timed cooldown after a successful check-in.

Scalable and Simple: Easy to add new students by simply adding their image and re-running the encoding script.

🛠️ Tech Stack
Backend: Python, Flask, Flask-SocketIO

Face Recognition: face_recognition, opencv-python

Database: SQLite

Frontend: HTML, CSS, JavaScript

Data Handling: pickle, Base64

Version Control: Git

🚀 Setup and Installation
Follow these steps to get the project up and running on your local machine.

1. Prerequisites
Make sure you have Python 3.8+ and Git installed on your system.

2. Clone the Repository
git clone [https://github.com/your-username/FaceCheck.git](https://github.com/your-username/FaceCheck.git)
cd FaceCheck

3. Set Up a Virtual Environment
It's highly recommended to use a virtual environment to manage project dependencies.

# Create a virtual environment
python -m venv venv

# Activate the virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

4. Install Dependencies
Install all the required Python packages using pip.

pip install -r requirements.txt

(Note: You will need to create a requirements.txt file. You can generate one by running pip freeze > requirements.txt after installing the packages mentioned previously: Flask, Flask-SocketIO, numpy, opencv-python, face_recognition, Pillow).

5. Add Student Images
Place the images of the students you want to register into the images/ folder. The filename for each image must be the student's unique ID (e.g., 123456.jpg, 234567.png).

6. Run the Setup Scripts
You need to run these scripts once to set up the database and generate the face encodings.

# 1. Create the database and add student details
python setup_database.py

# 2. Generate and save the face encodings from the images
python EncoderGenerator.py

7. Run the Application
Start the Flask web server.

python app.py

You should see output indicating that the server is running. Now, you can access the application!

🖥️ How to Use
Open your web browser (Chrome or Firefox is recommended).

Navigate to http://127.0.0.1:5000.

Allow the browser to access your webcam when prompted.

Position a registered student's face in front of the camera.

The status box on the webpage will update in real-time to confirm the attendance status.

📂 Project Structure
/FaceCheck/
|
|-- app.py                  # Main Flask web server
|-- EncoderGenerator.py     # Generates face encodings
|-- setup_database.py       # Sets up the SQLite database
|
|-- attendance.db           # SQLite database file
|-- EncodeFile.p            # Saved face encodings file
|
|-- images/                 # Folder for student images
|   |-- 123456.jpg
|   |-- ...
|
|-- templates/              # Folder for HTML files
|   |-- index.html
|
└── static/                 # Folder for static files (JS, CSS)
    └── script.js

💡 Future Improvements
Cloud Deployment: Deploy the application to a cloud service like Heroku or AWS.

Student Registration UI: Create a web page for administrators to add new students, upload their photos, and enter their details directly from the browser.

Attendance Dashboard: Build a dashboard to view attendance records, filter by date or student, and export reports.

Enhanced Security: Add user authentication for accessing the attendance dashboard or registration pages.

📄 License
This project is licensed under the MIT License. See the LICENSE file for details.
