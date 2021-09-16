from common.firebase import init_firebase
from firebase_admin import firestore
from datetime import datetime, timezone, timedelta

init_firebase()

def get_last_ranking(user, keyword, site):
  db = firestore.client()

  one_hour_ago = datetime.now(timezone.utc) - timedelta(hours = 1)
  last_ranking_stream = db.collection('ranking')\
    .where('user', '==', user)\
    .where('keyword', '==', keyword)\
    .where('rank_site', '==', site)\
    .where('timestamp', '<', one_hour_ago)\
    .order_by('timestamp', 'DESCENDING')\
    .limit(1)\
    .stream()

  last_ranking = next(last_ranking_stream, None)
  if last_ranking is None:
    return -1

  return last_ranking.to_dict()['position']
