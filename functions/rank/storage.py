from firebase_admin import firestore
from common.firebase import init_firebase

init_firebase()

def save(entry):
  timestamp = '{:%Y%m%d_%H%M%S_%f}'.format(entry['timestamp'])
  db = firestore.client()

  doc_ref = db.collection(u'ranking').document(timestamp)
  doc_ref.set(entry)