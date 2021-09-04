from common.firebase import init_firebase
from datetime import datetime
from firebase_admin import firestore

init_firebase()

def save_ranking(user, rank_site, keyword):
  db = firestore.client()

  user_doc = next(db.collection('users').where('email', '==', user.lower()).stream(), None)
  if user_doc is None:
    raise NoSuchUser()

  rankings = user_doc.get('rankings')

  existing = next(filter(lambda x: x['site'] == rank_site and x['keyword'] == keyword, rankings), None)
  if not existing is None:
    raise RankingExistsException()

  rankings.append({
    'site': rank_site,
    'keyword': keyword,
    'added': datetime.now()
  })

  user_doc.reference.update({
    'rankings': rankings
  })

class RankingExistsException(Exception):
  pass

class NoSuchUser(Exception):
  pass