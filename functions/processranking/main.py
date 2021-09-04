from publisher import publish
from storage import get_rankings
from datetime import datetime
import firebase_admin
from firebase_admin import credentials
import os

PROJECT_ID = os.getenv('GCP_PROJECT')
cred = credentials.ApplicationDefault()
firebase_admin.initialize_app(cred, {
  'projectId': PROJECT_ID,
})

def process_ranking(event, context):
  rankings = get_rankings()
  next = find_next_ranking(rankings)
  if next is None:
    print("No pending ranking found, skipping.")
    return

  print(f"Found {len(rankings)} pending rankings")
  rank_site = next['rank_site']
  keyword = next['keyword']
  print(f"Scheduling ranking for {rank_site} with keyword '{keyword}'")
  publish('rank', {
    'user': next['user'],
    'rank_site': rank_site,
    'keyword': keyword,
  })

def find_next_ranking(rankings):
  if len(rankings) == 0:
    return None

  sorted = list(rankings)
  sorted.sort(key=(lambda x: x['last_ranked'] or datetime(1, 1, 1)))
  return sorted[0]