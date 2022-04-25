import firebase_admin
from firebase_admin import credentials
import os

def init_firebase():
  if firebase_admin._apps:
    return

  EXPECTED_PROJECT_ID = 'seoranking-324303'
  PROJECT_ID = os.getenv('GCP_PROJECT')
  cred = credentials.ApplicationDefault()
  if PROJECT_ID is not None and PROJECT_ID != EXPECTED_PROJECT_ID:
    raise Exception('GCP_PROJECT environment variable not set to {}'.format(EXPECTED_PROJECT_ID))

  if PROJECT_ID is None and cred.project_id != EXPECTED_PROJECT_ID:
    raise Exception('Current credential project is set to {}, override with GCP_PROJECT env variable'.format(cred.project_id))

  firebase_admin.initialize_app(cred, {
    'projectId': PROJECT_ID,
  })

