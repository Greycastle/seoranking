import json
import base64


def encode_id(keyword: str, site: str, user: str) -> str:
  return base64.b64encode(json.dumps({'keyword': keyword, 'site': site, 'user': user}).encode()).decode()

def decode_id(id: str) -> list:
  data = json.loads(base64.b64decode(id.encode()).decode())
  return [ data['keyword'], data['site'], data['user'] ]