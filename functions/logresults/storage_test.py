from logresults.storage import get_rankings_count
from common.firebase import init_firebase
from firebase_admin import firestore

init_firebase()
db = firestore.client()

def test_can_count_when_no_ranks_are_saved():
  rankings_count = get_rankings_count(db, 'greycastle.se', 'missing keyword')
  assert rankings_count == 0

def test_can_count_when_there_are_ranks_saved():
  db = firestore.client()
  rankings_count = get_rankings_count(db, 'greycastle.se', 'greycastle')
  assert rankings_count > 0

