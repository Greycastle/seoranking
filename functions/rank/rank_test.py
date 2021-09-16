import base64
import json
import mock
from rank.rank import rank, get_position

mock_context = mock.Mock()

def test_rank():
  # data = {
  #   "user": "david@greycastle.se",
  #   "keyword": "greycastle",
  #   "rank_site": "greycastle.se"
  # }
  data = {
    "user": "david@greycastle.se",
    "keyword": "EDIFICE スクランブルスクエア店",
    "rank_site": "facy.jp"
  }

  message_contents = base64.b64encode(json.dumps(data).encode())
  event = {
    'data': message_contents
  }

  rank(event, mock_context)

def test_rank_position():
  entries = [
    { 'title': 'a', 'link': 'https://google.com' },
    { 'title': 'b', 'link': 'https://greycastle.se' },
    { 'title': 'c', 'link': 'https://yahoo.com' }
  ]

  assert get_position(results=entries, rank_site='greycastle.se') == 2

def test_not_ranking():
  entries = [
    { 'title': 'a', 'link': 'https://google.com' }
  ]

  assert get_position(results=entries, rank_site='greycastle.se') == None