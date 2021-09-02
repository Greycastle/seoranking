import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import datetime
import os

PROJECT_ID = os.getenv('GCP_PROJECT')
cred = credentials.ApplicationDefault()
firebase_admin.initialize_app(cred, {
  'projectId': PROJECT_ID,
})
db = firestore.client()

def exists(username):
  doc = next(db.collection('users').where('email', '==', username.lower()).stream(), None)
  return doc != None

def register_new_user(username, keyword, rank_site):
  if exists(username):
    raise UserAlreadyAdded()

  DEFAULT_RANKS=30
  now = datetime.datetime.now()
  user = {
    'email': username.lower(),
    'added': now,
    'ranks_left': DEFAULT_RANKS,
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