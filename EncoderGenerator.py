import os
import pickle
import cv2
import face_recognition

# --- Firebase related code is REMOVED ---

# Path to the folder containing student images
folderPath = 'images'
imgList = os.listdir(folderPath)

# Store the images and student IDs in lists
ImgList = []
studentIds = []

for path in imgList:
    imagePath = os.path.join(folderPath, path)
    ImgList.append(cv2.imread(imagePath))
    # Extract student ID from the filename (e.g., 123456.jpg -> 123456)
    studentIds.append(os.path.splitext(path)[0])

print(f"Loaded {len(ImgList)} images.")
print(f"Student IDs found: {studentIds}")

def findEncodings(imagesList):
    """Encodes a list of images."""
    Encodings = []
    for img in imagesList:
        # Convert image from BGR to RGB
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        try:
            # Find the face encoding
            encoding = face_recognition.face_encodings(img)[0]
            Encodings.append(encoding)
        except IndexError:
            print(f"Warning: No face found in one of the images. It will be skipped.")
    return Encodings

print("Encoding Started...")
encodeListKnown = findEncodings(ImgList)
encodeListKnownWithIds = [encodeListKnown, studentIds]
print("Encoding Complete.")

# Save the encodings and student IDs to a pickle file
print('Saving encoding file...')
with open('EncodeFile.p', 'wb') as file:
    pickle.dump(encodeListKnownWithIds, file)
print('File "EncodeFile.p" saved successfully!')