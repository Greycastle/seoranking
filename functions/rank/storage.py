import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import os
import datetime

def save(entry):
  PROJECT_ID = os.getenv('GCP_PROJECT')
  cred = credentials.ApplicationDefault()
  firebase_admin.initialize_app(cred, {
    'projectId': PROJECT_ID,
  })

  timestamp = '{:%Y%m%d_%H%M%S_%f}'.format(datetime.datetime.now())
  db = firestore.client()

  doc_ref = db.collection(u'ranking').document(timestamp)
  doc_ref.set(entry)