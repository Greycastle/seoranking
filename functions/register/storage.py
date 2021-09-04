from firebase_admin import firestore
from common.firebase import init_firebase
import datetime

init_firebase()
db = firestore.client()

def exists(username):
  doc = next(db.collection('users').where('email', '==', username.lower()).stream(), None)
  return doc != None

def register_new_user(username, keyword, rank_site):
  if exists(username):
    raise UserAlreadyAdded()

  DEFAULT_RANKS=30
  DEFAULT_SCHEDULE_DAYS=1
  now = datetime.datetime.now()
  user = {
    'email': username.lower(),
    'added': now,
    'ranks_left': DEFAULT_RANKS,
    'days_schedule': DEFAULT_SCHEDULE_DAYS,
    'rankings': [
      {
        'site': rank_site,
        'keyword': keyword,
        'added': now
      }
    ]
  }
  db.collection(u'users').add(user)

class UserAlreadyAdded(Exception):
  pass