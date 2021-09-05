
from firebase_admin import auth
from common.http import bad_request, unauthorized
from stats.data_source import read_stats, NoSuchUser
import re
import logging
from common.firebase import init_firebase

logger = logging.getLogger(__name__)

init_firebase()

def get_stats(request):
  if request.method == 'OPTIONS':
    headers = {
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': 'GET, OPTION',
            'Access-Control-Allow-Headers': 'Content-Type, Authorization',
            'Access-Control-Max-Age': '3600'
        }
    return ('', 204, headers)

  headers = { 'Access-Control-Allow-Origin': '*' }
  if not request.headers.get('authorization'):
      unauthorized('No authorization token provided', headers)
  try:
      pattern  = re.compile("Bearer ", re.IGNORECASE)
      token = pattern.sub("", request.headers['authorization'])
      request.user = auth.verify_id_token(token)
  except Exception as e:
      logger.error("Invalid auth token", exc_info=e)
      bad_request('Invalid authorization token', headers)

  try:
    data = read_stats(request.user['email'])
    return (data, 200, headers)
  except(NoSuchUser):
    return ('No user found', 404, headers)