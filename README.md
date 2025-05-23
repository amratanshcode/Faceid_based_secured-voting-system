# FaceID-Based Secured Voting System

The FaceID-Based Secured Voting System is a Python application designed to modernize the voting process through biometric verification.
By using facial recognition, this system eliminates traditional methods like ID cards or manual voter lists, ensuring that each vote is tied to a verified individual.
The project combines computer vision, machine learning, and real-time interaction to deliver a secure, user-friendly experience that could serve as a prototype for future digital 
voting platforms.

---

## Features

- Face-based user authentication
- K-Nearest Neighbors (KNN) face recognition
- Real-time webcam capture using OpenCV
- Vote logging with timestamps in CSV
- Text-to-speech feedback
- Simple data storage with Pickle

---

## Technologies Used

- Python
- OpenCV
- NumPy
- scikit-learn (KNN)
- pickle for face data storage
- win32com.client for voice feedback (Windows only)

---

## Project Structure

Faceid_based_secured-voting-system/
├── add_faces.py # Register user faces
├── give_vote.py # Verify and vote via face recognition
├── Votes.csv # Log of all votes cast
├── data/ # Pickled face data and IDs
├── background*.png # Background images for UI
├── requirement.txt # Dependencies
└── .idea/.vscode/ # IDE settings

yaml
Copy
Edit

---

## How to Run

### 1. Install Dependencies
```bash
pip install -r requirement.txt
2. Register a Face
bash
Copy
Edit
python add_faces.py
3. Cast a Vote
bash
Copy
Edit
python give_vote.py
Press q to exit the camera interface.

Notes
Ensure a webcam is connected and working properly.

This project is developed for Windows due to its use of the win32com.client text-to-speech library.

Each voter is identified by their Aadhaar number and face image.

Contributions
Pull requests are welcome. Feel free to contribute by improving functionality, fixing bugs, or enhancing the user interface.

MADE BY - @amratanshcode, @
