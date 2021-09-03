import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import os

def get_rankings():
  PROJECT_ID = os.getenv('GCP_PROJECT')
  cred = credentials.ApplicationDefault()
  firebase_admin.initialize_app(cred, {
    'projectId': PROJECT_ID,
  })

  db = firestore.client()

  active_users = db.collection('users').where('ranks_left', '>', 0).stream()
  rankings = []
  for user_ref in active_users:
    user = user_ref.to_dict()
    user_rankings = user.get('rankings', None)
    email = user['email']
    if user_rankings is None:
      continue

    for user_ranking in user_rankings:
      rankings.append({
        'user': email,
        'keyword': user_ranking['keyword'],
        'rank_site': user_ranking['site'],
        'last_ranked': user_ranking.get('last_ranked', None)
      })

  return rankings