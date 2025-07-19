# FaceCheck: Real-Time Web-Based Attendance System

<div align="center">

![FaceCheck Banner](https://placehold.co/1200x400/2c3e50/FFFFFF?text=FaceCheck&font=raleway)

**A modern, real-time attendance system that uses facial recognition through a simple web interface.**

![Python Version](https://img.shields.io/badge/Python-3.8%2B-blue.svg)
![Flask Framework](https://img.shields.io/badge/Framework-Flask-green.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)
![Project Status](https://img.shields.io/badge/status-active-brightgreen)

</div>

## Overview

FaceCheck leverages your webcam to create a seamless and efficient attendance-taking process, eliminating the need for manual check-ins. Built with Python and Flask, it's designed to be simple, scalable, and run entirely on your local machine with complete privacy protection.

## ✨ Key Features

- **🚀 Real-Time Recognition**: Instantly detects and identifies registered students from a live webcam feed
- **🌐 Web-Based Interface**: Accessible from any modern browser on your local network - no desktop app needed
- **🔒 Local Data Storage**: Ensures privacy and offline functionality by storing all data locally using SQLite
- **💡 Dynamic Feedback**: Provides immediate visual confirmation for marked attendance, duplicates, or unknown faces
- **⏱️ Cooldown Period**: Prevents accidental duplicate entries with a timed cooldown after successful check-in
- **🌱 Scalable & Simple**: Easily add new students by adding their image and re-running a single script

## 🛠️ Technology Stack

| Category | Technologies |
|----------|-------------|
| **Backend** | Python, Flask, Flask-SocketIO |
| **Face Recognition** | face_recognition, opencv-python, Pillow |
| **Database** | SQLite |
| **Frontend** | HTML5, CSS3, JavaScript |
| **Data Handling** | pickle, Base64 |
| **Development** | Git, Virtual Environments |

## 🚀 Getting Started

### Prerequisites

Before you begin, ensure you have the following installed:
- Python 3.8 or higher
- Git
- A working webcam
- Modern web browser

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/your-username/FaceCheck.git
   cd FaceCheck
   ```

2. **Create and activate a virtual environment:**
   ```bash
   # Create the environment
   python -m venv venv
   
   # Activate it
   # Windows:
   venv\Scripts\activate
   # macOS/Linux:
   source venv/bin/activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

### System Setup

1. **Add Student Images:**
   - Place student images in the `images/` directory
   - Name each file with the student's unique ID (e.g., `123456.jpg`)
   - Ensure images are clear and show the face prominently

2. **Initialize the System:**
   ```bash
   # Create database and add student records
   python setup_database.py
   
   # Generate face encodings from images
   python EncoderGenerator.py
   ```

3. **Launch the Application:**
   ```bash
   python app.py
   ```

4. **Access the Application:**
   - Open your browser and navigate to `http://127.0.0.1:5000`
   - Allow camera permissions when prompted

## 📂 Project Structure

```
FaceCheck/
├── .gitignore
├── app.py                 # Main Flask application
├── EncoderGenerator.py    # Face encoding generator
├── setup_database.py     # Database initialization
├── requirements.txt       # Python dependencies
├── README.md
├── attendance.db          # SQLite database (generated)
├── EncodeFile.p          # Encoded faces data (generated)
├── images/               # Student images directory
│   └── 123456.jpg
├── static/
│   └── script.js         # Frontend JavaScript
└── templates/
    └── index.html        # Main web interface
```

## 📋 Requirements

Create a `requirements.txt` file with the following dependencies:

```
Flask==2.3.3
Flask-SocketIO==5.3.6
numpy==1.24.3
opencv-python==4.8.1.78
face-recognition==1.3.0
Pillow==10.0.1
```

## 🎯 Usage

1. **Adding New Students:**
   - Add student photo to `images/` folder with ID as filename
   - Run `python setup_database.py` to update database
   - Run `python EncoderGenerator.py` to update face encodings
   - Restart the application

2. **Taking Attendance:**
   - Access the web interface
   - Position yourself in front of the camera
   - The system will automatically detect and mark attendance
   - View real-time feedback on the interface

## 🔧 Configuration

The application uses default settings that work well for most scenarios. For advanced configuration:

- Modify camera settings in `app.py`
- Adjust recognition sensitivity parameters
- Customize cooldown periods
- Modify database schema in `setup_database.py`

## 🚨 Troubleshooting

**Camera not detected:**
- Ensure camera permissions are granted
- Check if other applications are using the camera
- Verify camera drivers are installed

**Face not recognized:**
- Ensure good lighting conditions
- Check image quality in the `images/` folder
- Re-run `EncoderGenerator.py` after adding new images

**Performance issues:**
- Reduce video resolution in settings
- Ensure adequate system resources
- Close unnecessary applications

## 🤝 Contributing

We welcome contributions! Here's how you can help:

1. Fork the project
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

### Development Guidelines

- Follow PEP 8 style guidelines
- Write clear commit messages
- Add comments for complex logic
- Test your changes thoroughly
- Update documentation as needed

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- [face_recognition](https://github.com/ageitgey/face_recognition) library by Adam Geitgey
- [Flask](https://flask.palletsprojects.com/) framework
- [OpenCV](https://opencv.org/) computer vision library

## 📞 Support

If you encounter any issues or have questions:

1. Check the [Issues](https://github.com/your-username/FaceCheck/issues) section
2. Create a new issue with detailed information
3. Include error messages and system information

---

<div align="center">
<strong>Made with ❤️ for educational institutions and organizations</strong>
</div>
