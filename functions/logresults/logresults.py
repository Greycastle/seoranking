from datetime import datetime
from logresults.storage import bill_user, log_latest_result
from firebase_admin import firestore
from common.firebase import init_firebase

init_firebase()

def log_ranking_results(event, context):
  if not 'data' in event:
    print("No data in event, skipping")
    return

  import base64
  import json

  db = firestore.client()

  message = json.loads(base64.b64decode(event['data']).decode('utf-8'))
  user = message['user']
  keyword = message['keyword']
  rank_site = message['rank_site']
  timestamp = datetime.fromisoformat(message['timestamp'])
  rank = message['position']
  lastRankingDocPath = message.get('rankingDocPath', None)

  log_latest_result(db, user, keyword, rank_site, rank, timestamp, lastRankingDocPath)
  bill_user(db, user)