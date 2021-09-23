from common.http import not_found, bad_request, enable_cors, require_auth
from stats.data_source import read_stats, NoSuchUser, read_detailed_stats, NoSuchEntry
from common.firebase import init_firebase
import base64
import logging

logger = logging.getLogger(__name__)

init_firebase()

@enable_cors
@require_auth
def get_stats(request):
  try:
    return read_stats(request.user['email'])
  except(NoSuchUser):
    not_found('No such user found')

@enable_cors
def get_public_stats(request):
  try:
    id = request.args.get('id', None)
    if id is None:
      bad_request('Missing id attribute')
    email = base64.b64decode(id.encode()).decode()
    stats = read_stats(email)
    stats.pop('stats')
    return stats
  except(NoSuchUser):
    not_found('No such user found')

@enable_cors
def get_detailed_stats(request):
  id = request.args.get('id')
  try:
    return read_detailed_stats(id)
  except(NoSuchEntry):
    not_found('No such entry found')