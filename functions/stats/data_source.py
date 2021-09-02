import base64
from firebase_admin import firestore
import json

def read_stats(user_name):
  db = firestore.client()
  user = next(db.collection('users').where('email', '==', user_name).stream(), None)
  if user is None:
    raise NoSuchUser()

  data = user.to_dict()

  items = list(map(lambda x: { 'keyword': x['keyword'], 'site': x['site'] }, data.get('rankings', [])))

  rankings = list(map(lambda x: x.to_dict(), db.collection("ranking").where("user", "==", user_name).stream()))
  print(f"got {len(rankings)} rankings for {user_name}")

  for item in items:
    items_rankings = list(find_rankings(item['keyword'], item['site'], rankings))
    items_rankings.sort(key=(lambda x: x['timestamp']))
    item['rankings'] = len(items_rankings)
    item['downloadId'] = base64.b64encode(json.dumps({'keyword': item['keyword'], 'site': item['site'], 'user': user_name}).encode()).decode()
    if (len(items_rankings) > 0):
      recent = items_rankings[0]
      item['lastRanking'] = recent['position']
      item['lastConfirmed'] = recent['timestamp'].isoformat()

  return {
    "stats": {
      "creditsSpent": data.get('ranks_used', 0),
      "creditsLeft": data.get('ranks_left', 0),
      "schedule": data.get('schedule', 3)
    },
    "items": items
  }

def find_rankings(keyword, site, all_rankings):
  for ranking in all_rankings:
    if keyword != ranking['keyword'] or site != ranking['rank_site']:
      continue

    yield ranking

class NoSuchUser(Exception):
  pass