from google_search import run_search
from publisher import publish
from storage import save
from datetime import datetime

def rank(event, context):

  if not 'data' in event:
    print("No data in event, skipping")
    return

  import base64
  import json

  # for who?
  message = json.loads(base64.b64decode(event['data']).decode('utf-8'))
  user = message['user']
  keyword = message['keyword']
  rank_site = message['rank_site']

  print(f"Trigger a ranking of {rank_site} for keyword '{keyword}' for user {user}")

  ranking = run_search(query=keyword, stop_on=rank_site)
  print(f"Got {len(ranking)} responses for ranking")

  ## save rank
  results = {
    'user': user,
    'keyword': keyword,
    'rank_site': rank_site,
    'timestamp': datetime.now(),
    'position': get_position(results=ranking, rank_site=rank_site),
    'results': ranking
  }
  save(results)

  # trigger that rank is saved
  results['timestamp'] = results['timestamp'].isoformat()
  publish('ranking-results', results)

def get_position(results, rank_site):
  position = 1
  for result in results:
    if rank_site.lower() in result['link'].lower():
      return position
    position += 1

  return None