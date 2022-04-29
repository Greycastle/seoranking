from firebase_admin import firestore
from common.ranking_id import decode_id, encode_id

def read_stats(user_name):
  db = firestore.client()
  user = next(db.collection('users').where('email', '==', user_name).stream(), None)
  if user is None:
    raise NoSuchUser()

  data = user.to_dict()

  items = []
  for ranking_data in data.get('rankings', []):
    item = {
      'keyword': ranking_data['keyword'],
      'site': ranking_data['site']
    }
    items.append(item)
    item['rankings'] = ranking_data.get('total_ranks', 0)
    item['downloadId'] = encode_id(ranking_data['keyword'], ranking_data['site'], user_name)
    last_ranking_path = ranking_data.get('last_ranking_path', None)
    print(f"last_ranking_path: {last_ranking_path}")
    if last_ranking_path is not None:
      last_ranking = get_recent_ranking(db, last_ranking_path)
      item['lastRanking'] = last_ranking['lastRanking']
      item['lastConfirmed'] = last_ranking['lastConfirmed']

  return {
    "stats": {
      "creditsSpent": data.get('ranks_used', 0),
      "creditsLeft": data.get('ranks_left', 0),
      "schedule": data.get('schedule', 3)
    },
    "items": items
  }

def get_recent_ranking(db, path):
  print(f'Reading recent ranking from {path}')
  ranking = db.document(path).get()
  if ranking.exists:
    data = ranking.to_dict()
    return {
      'lastRanking': data['position'],
      'lastConfirmed': data['timestamp'].isoformat()
    }

  print('Not found!')
  return {
    'lastRanking': None,
    'lastConfirmed': None
  }

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

  entries = list(map(lambda x: x.to_dict(), stream))
  stats = list(map(lambda x: { 'date': x['timestamp'].isoformat(), 'rank': x['position'] }, entries))
  if len(stats) == 0:
    print(f"No entries for keyword '{keyword}', site '{site}' and user '{user}'")
    raise NoSuchEntry()

  return {
    "ranking": {
      "keyword": keyword,
      "site": site
    },
    "competitors": list(entries[0]['results']),
    "stats": stats
  }

class NoSuchUser(Exception):
  pass

class NoSuchEntry(Exception):
  pass