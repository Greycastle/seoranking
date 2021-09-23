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
    item['downloadId'] = encode_id(item['keyword'], item['site'], user_name)
    if (len(items_rankings) > 0):
      recent = items_rankings[-1]
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

def encode_id(keyword: str, site: str, user: str) -> str:
  return base64.b64encode(json.dumps({'keyword': keyword, 'site': site, 'user': user}).encode()).decode()

def decode_id(id: str) -> list:
  data = json.loads(base64.b64decode(id.encode()).decode())
  return [ data['keyword'], data['site'], data['user'] ]

def find_rankings(keyword, site, all_rankings):
  for ranking in all_rankings:
    if keyword != ranking['keyword'] or site != ranking['rank_site']:
      continue

    yield ranking


def read_detailed_stats(id: str):
  keyword, site, user = decode_id(id)

  db = firestore.client()
  stream = db.collection('ranking')\
    .where('user', '==', user)\
    .where('keyword', '==', keyword)\
    .where('rank_site', '==', site)\
    .order_by('timestamp', 'DESCENDING')\
    .limit(100)\
    .stream()


  first_entry = next(stream, None)
  if first_entry is None:
    print(f"No entry for keyword '{keyword}', site '{site}' and user '{user}'")
    raise NoSuchEntry()

  stats = list(map(lambda x: { 'date': x.to_dict()['timestamp'].isoformat(), 'rank': x.to_dict()['position'] } ,stream))
  stats.insert(0, first_entry) # put it back in

  return {
    "ranking": {
      "keyword": keyword,
      "site": site
    },
    "competitors": list(first_entry.to_dict()['results']),
    "stats": stats
  }

class NoSuchUser(Exception):
  pass

class NoSuchEntry(Exception):
  pass