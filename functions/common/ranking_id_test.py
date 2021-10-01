from base64 import decode, encode
from common.ranking_id import encode_id, decode_id

def test_encoding():
  keyword = '日本語のキーワード'
  site = 'greycastle.se'
  user = 'test@greycastle.se'

  encoded = encode_id(keyword, site, user)
  decoded_kw, decoded_site, decoded_user = decode_id(encoded)

  assert site == decoded_site
  assert keyword == decoded_kw
  assert user == decoded_user