import firebase_admin
from firebase_admin import credentials
import os

def init_firebase():
  if firebase_admin._apps:
    return

  PROJECT_ID = os.getenv('GCP_PROJECT')
  cred = credentials.ApplicationDefault()
  firebase_admin.initialize_app(cred, {
    'projectId': PROJECT_ID,
  })