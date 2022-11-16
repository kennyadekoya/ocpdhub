

from flask import Flask, render_template, request


from flask import redirect
from pyrebase import pyrebase
import pyrebase
import firebase_admin
from firebase_admin import credentials
from firebase_admin import auth
from firebase_admin import firestore
import smtplib
import pandas as pd

firebaseConfig = {
    "apiKey": "AIzaSyB9DaUxj2YCDMrNTOSgxpF49e6B5lCgOMA",
    "authDomain": "datahub-21e7e.firebaseapp.com",
    "databaseURL": "https://datahub-21e7e-default-rtdb.firebaseio.com",
    "projectId": "datahub-21e7e",
    "storageBucket": "datahub-21e7e.appspot.com",
    "messagingSenderId": "166143497203",
    "appId": "1:166143497203:web:4cf11ad5cfec0214ee7886",
    "measurementId": "G-6Z3W87LP23"
}

app = Flask(__name__)
app.config['SERVER_NAME'] = 'localhost:5000'


# defining the url or route for the website
#@app.route('/fiskocpddatahub')
cred = credentials.Certificate('firebase-sdk.json')
firebase_admin.initialize_app(cred)

db = firestore.client()
userid = ''
fisk_email = "Boobennet@my.fisk.edu"
fisk_email= fisk_email.title()
year = "2022"
semester = "Fall"
Opportunity = "Undergraduate: Internship Opportunity"
if 'My.Fisk.Edu' in fisk_email:
    for i in fisk_email:
        if i != '@':
            userid = userid + i
        elif i == '@':
            break
    result = db.collection('student').document(str(userid)).get()
    result = result.to_dict()
    first_name = result.get('First Name')
    first_name = first_name.lower()
    first_name = first_name.title()
    last_name = result.get('Last Name')
    last_name = last_name.lower()
    last_name = last_name.title()

    doc_ref = db.collection('student').document(str(userid))
    docs = doc_ref.collection(str(year)).get()
    # print(docs.to_dict())
    if Opportunity == "Undergraduate: Internship Opportunity" and semester == "Fall":
        docs = doc_ref.collection(str(year)).document('Fall Internship Information').get()
        info_doc = docs.to_dict()
        if info_doc:
            grade = info_doc['Classification']
            year = info_doc['Internship Year']
            company_name = info_doc['Company Name']
            pay = info_doc['Hourly Pay']
            position = info_doc['Position']
        else:
            grade = ""
            year = ""
            company_name = ""
            pay = ""
            position = ""
    print(first_name + " " + last_name)
    print(grade)