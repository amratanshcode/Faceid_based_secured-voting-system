import csv
import os
import pickle
import time
from datetime import datetime

import cv2
from sklearn.neighbors import KNeighborsClassifier
from win32com.client import Dispatch


def speak(str1):
    speak=Dispatch(("SAPI.SpVoice"))
    speak.Speak(str1)

video = cv2.VideoCapture(0)

facedetect = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
if not os.path.exists('data/'):
    os.makedirs('data/')

with open('data/names.pkl', 'rb') as f:
    LABELS = pickle.load(f)

with open('data/faces_data.pkl', 'rb') as f:
    FACES = pickle.load(f)

knn = KNeighborsClassifier(n_neighbors=5)

min_len = min(len(FACES), len(LABELS))
FACES = FACES[:min_len]
LABELS = LABELS[:min_len]

knn.fit(FACES, LABELS)
imgBackground = cv2.imread("background11111.png")
mgBackground = cv2.resize(imgBackground, (640, 480))

COL_NAMES = ['NAME', 'VOTE', 'DATE', 'TIME']

while True:
    ret, frame = video.read()
    if not ret or frame is None:
        print( "Failed to grab frame from webcam." )
        continue

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = facedetect.detectMultiScale( gray, 1.3, 5 )
    for (x, y, w, h) in faces:
        crop_img = frame[y:y + h, x:x + w]
        resized_img = cv2.resize( crop_img, (50, 50) ).flatten().reshape( 1, -1 )
        output = knn.predict( resized_img )
        ts = time.time()
        date = datetime.fromtimestamp( ts ).strftime( "%d-%m-%Y" )
        timestamp = datetime.fromtimestamp( ts ).strftime( "%H:%M-%S" )
        exist = os.path.isfile( "Votes.csv" )
        cv2.rectangle( frame, (x, y), (x + w, y + h), (0, 0, 255), 1 )
        cv2.rectangle( frame, (x, y), (x + w, y + h), (50, 50, 255), 2 )
        cv2.rectangle( frame, (x, y - 40), (x + w, y), (50, 50, 255), -1 )
        cv2.putText( frame, str( output[0] ), (x, y - 15), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 1 )
        cv2.rectangle( frame, (x, y), (x + w, y + h), (50, 50, 255), 1 )

    imgBackground[370:370 + 480, 225:225 + 640] = frame
    cv2.imshow( 'frame', imgBackground )
    k = cv2.waitKey( 1 )


    def check_if_exists(voter_id):
        """
        Checks if a voter ID already exists in the Votes.csv file.
        Returns True if it exists, otherwise False.
        """
        if not os.path.exists( "Votes.csv" ):
            speak("Voters doesn't exist in database") # If file doesn't exist, no one has voted yet


    if k == ord( '1' ):
        speak( "YOUR VOTE HAS BEEN RECORDED" )
        time.sleep( 5 )
        if exist:
            with open( "Votes.csv", "a" ) as csvfile:
                writer = csv.writer( csvfile )
                attendance = [output[0], "BJP", date, timestamp]
                writer.writerow( attendance )
        else:
            with open( "Votes.csv", "a" ) as csvfile:
                writer = csv.writer( csvfile )
                writer.writerow( COL_NAMES )
                attendance = [output[0], "BJP", date, timestamp]
                writer.writerow( attendance )
        speak( "THANK YOU FOR PARTICIPATING IN THE ELECTIONS" )
        break

    if k == ord( '2' ):
        speak( "YOUR VOTE HAS BEEN RECORDED" )
        time.sleep( 5 )
        if exist:
            with open( "Votes.csv", "a" ) as csvfile:
                writer = csv.writer( csvfile )
                attendance = [output[0], "CONGRESS", date, timestamp]
                writer.writerow( attendance )
        else:
            with open( "Votes.csv", "a" ) as csvfile:
                writer = csv.writer( csvfile )
                writer.writerow( COL_NAMES )
                attendance = [output[0], "CONGRESS", date, timestamp]
                writer.writerow( attendance )
        speak( "THANK YOU FOR PARTICIPATING IN THE ELECTIONS" )
        break

    if k == ord( '3' ):
        speak( "YOUR VOTE HAS BEEN RECORDED" )
        time.sleep( 5 )
        if exist:
            with open( "Votes.csv", "a" ) as csvfile:
                writer = csv.writer( csvfile )
                attendance = [output[0], "AAP", date, timestamp]
                writer.writerow( attendance )
        else:
            with open( "Votes.csv", "a" ) as csvfile:
                writer = csv.writer( csvfile )
                writer.writerow( COL_NAMES )
                attendance = [output[0], "AAP", date, timestamp]
                writer.writerow( attendance )
        speak( "THANK YOU FOR PARTICIPATING IN THE ELECTIONS" )
        break

    if k == ord( '4' ):
        speak( "YOUR VOTE HAS BEEN RECORDED" )
        time.sleep( 5 )
        if exist:
            with open( "Votes.csv", "a" ) as csvfile:
                writer = csv.writer( csvfile )
                attendance = [output[0], "NOTA", date, timestamp]
                writer.writerow( attendance )
        else:
            with open( "Votes.csv", "a" ) as csvfile:
                writer = csv.writer( csvfile )
                writer.writerow( COL_NAMES )
                attendance = [output[0], "NOTA", date, timestamp]
                writer.writerow( attendance )
        speak( "THANK YOU FOR PARTICIPATING IN THE ELECTIONS" )
        break

video.release()
cv2.destroyAllWindows()