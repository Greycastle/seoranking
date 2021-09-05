from common.publisher import publish
from common.http import require_auth, enable_cors
from addranking.storage import save_ranking, RankingExistsException

@enable_cors
@require_auth
def handle_add_ranking_request(request):
  data = request.get_json()
  publish('add-ranking', {
    'user': request.user['email'],
    'keyword': data['keyword'],
    'rank_site': data['rank_site']
  })

  return 'ok'

def handle_add_ranking_event(event, context):
  if not 'data' in event:
    print("No data in event, skipping")
    return

  import base64
  import json

  message = json.loads(base64.b64decode(event['data']).decode('utf-8'))
  user = message['user']
  keyword = message['keyword']
  rank_site = message['rank_site']

  try:
    save_ranking(user, rank_site, keyword)

    publish('rank', {
      'user': user,
      'rank_site': rank_site,
      'keyword': keyword
    })
  except RankingExistsException:
    print(f"Ranking for site {rank_site} with keyword '{keyword}' already exists, skipping..")