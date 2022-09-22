from rank.google_search import run_search

def test_search():
  result = run_search(query='greycastle', stop_on="greycastle.se")
  urls = list(map(lambda x: x['link'], result))
  assert "https://www.greycastle.se/" in urls
