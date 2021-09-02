import base64
import json
import mock
from rank import main

mock_context = mock.Mock()

def test_rank():
  data = {
    "user": "david@greycastle.se",
    "keyword": "greycastle",
    "rank_site": "greycastle.se"
  }

  message_contents = base64.b64encode(json.dumps(data).encode())

  #main.rank(event, mock_context)

def test_rank_position():
  entries = [
    { 'title': 'a', 'link': 'https://google.com' },
    { 'title': 'b', 'link': 'https://greycastle.se' },
    { 'title': 'c', 'link': 'https://yahoo.com' }
  ]

  assert main.get_position(entries, 'greycastle.se') == 2

def test_not_ranking():
  entries = [
    { 'title': 'a', 'link': 'https://google.com' }
  ]

  assert main.get_position(entries, 'greycastle.se') == None