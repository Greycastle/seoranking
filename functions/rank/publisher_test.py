from rank.publisher import publish

def test_publish():
  # just check if it works, if you need to validate, do so manually
  publish('general', { 'key': 'value' })