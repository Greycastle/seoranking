import base64
import json

def get_event_from_dict(data):
  return {
    'data': base64.b64encode(json.dumps(data).encode()).decode()
  }