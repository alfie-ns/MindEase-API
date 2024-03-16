# This file is used to initialize the firebase admin SDK

import firebase_admin
from firebase_admin import credentials

cred = credentials.Certificate("/Users/alfienurse/Library/CloudStorage/GoogleDrive-alfienurse@gmail.com/My Drive/Dev/MindEase Dev/mindease-d130d-firebase-adminsdk-pvc13-7d4cdaf4ce.json")
firebase_admin.initialize_app(cred)