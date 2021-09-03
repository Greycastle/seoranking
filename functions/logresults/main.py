from datetime import datetime
from storage import bill_user, log_latest_result
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import os

def log_ranking_results(event, context):
  if not 'data' in event:
    print("No data in event, skipping")
    return

  import base64
  import json

  PROJECT_ID = os.getenv('GCP_PROJECT')
  cred = credentials.ApplicationDefault()
  firebase_admin.initialize_app(cred, {
    'projectId': PROJECT_ID,
  })

  db = firestore.client()

  message = json.loads(base64.b64decode(event['data']).decode('utf-8'))
  user = message['user']
  keyword = message['keyword']
  rank_site = message['rank_site']
  timestamp = datetime.fromisoformat(message['timestamp'])
  rank = message['position']

  log_latest_result(db, user, keyword, rank_site, rank, timestamp)
  bill_user(db, user)