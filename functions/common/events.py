import base64
import json

def get_event_data(event, default=None, throw=True):
  if 'data' in event:
    return json.loads(base64.b64decode(event['data']).decode('utf-8'))

  if throw:
    raise NoDataInEvent()

  return default

class NoDataInEvent(Exception):
  pass