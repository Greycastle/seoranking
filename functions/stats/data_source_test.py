from stats.data_source import encode_id, decode_id

def test_encode_decode_id():
  b64_str = encode_id('some keywords', 'a.site', 'some@user.com')
  keyword, site, user = decode_id(b64_str)

  assert keyword == 'some keywords'
  assert site == 'a.site'
  assert user == 'some@user.com'