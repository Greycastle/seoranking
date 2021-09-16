from notifyranking.storage import get_last_ranking

def test_get_ranking():
  ranking = get_last_ranking('david@greycastle.se', 'greycastle', 'greycastle.se')
  assert ranking > 0

def test_get_ranking_if_missing():
  ranking = get_last_ranking('david@greycastle.se', 'missing', 'greycastle.se')
  assert ranking == -1