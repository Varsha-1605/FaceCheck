import base64
import io
import cv2
import numpy as np
import pickle
import sqlite3
from datetime import datetime
from PIL import Image
from flask import Flask, render_template
from flask_socketio import SocketIO, emit
import face_recognition

# Initialize Flask app and SocketIO
app = Flask(__name__)
socketio = SocketIO(app)

# --- Load Face Encodings ---
print('Loading Encodings...')
with open('EncodeFile.p', 'rb') as file:
    encodeListKnownWithIds = pickle.load(file)
encodeListKnown, studentIds = encodeListKnownWithIds
print("Encoding Loaded successfully.")

def db_connect():
    """Establishes a connection to the SQLite database."""
    return sqlite3.connect('attendance.db')

@app.route('/')
def index():
    """Renders the main web page."""
    return render_template('index.html')

@socketio.on('image')
def handle_image(data_image):
    """Handles image data received from the client for face recognition."""
    # Decode the base64 image
    sbuf = io.StringIO()
    sbuf.write(data_image)
    b = io.BytesIO(base64.b64decode(data_image.split(',')[1]))
    pimg = Image.open(b)
    frame = cv2.cvtColor(np.array(pimg), cv2.COLOR_RGB2BGR)

    # Find faces and encodings in the current frame
    faceCurrFrame = face_recognition.face_locations(frame)
    encodeCurrFrame = face_recognition.face_encodings(frame, faceCurrFrame)

    response = {'status': 'No Face Detected'} # Default response

    if not faceCurrFrame:
        emit('response', response)
        return

    for encodeFace, faceLoc in zip(encodeCurrFrame, faceCurrFrame):
        matches = face_recognition.compare_faces(encodeListKnown, encodeFace)
        faceDis = face_recognition.face_distance(encodeListKnown, encodeFace)
        
        matchIndex = np.argmin(faceDis)

        if matches[matchIndex]:
            student_id = studentIds[matchIndex]
            
            conn = db_connect()
            cursor = conn.cursor()
            cursor.execute("SELECT name, last_attendance_time, total_attendance FROM students WHERE id = ?", (student_id,))
            student_data = cursor.fetchone()
            
            if student_data:
                name, last_time_str, attendance_count = student_data
                last_time = datetime.strptime(last_time_str, "%Y-%m-%d %H:%M:%S")
                seconds_elapsed = (datetime.now() - last_time).total_seconds()
                
                # Cooldown of 60 seconds to prevent multiple entries
                if seconds_elapsed > 60:
                    new_attendance = attendance_count + 1
                    current_time_str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                    cursor.execute("UPDATE students SET total_attendance = ?, last_attendance_time = ? WHERE id = ?",
                                   (new_attendance, current_time_str, student_id))
                    conn.commit()
                    response = {'status': 'Attendance Marked!', 'name': name, 'id': student_id}
                else:
                    response = {'status': 'Already Marked Today', 'name': name, 'id': student_id}
            
            conn.close()
        else:
            response = {'status': 'Unknown Face Detected'}
        
        # Send the response back to the client
        emit('response', response)
        return # Process only one face per frame for simplicity

if __name__ == '__main__':
    print("Starting server... Go to http://127.0.0.1:5000")
    socketio.run(app, debug=True)