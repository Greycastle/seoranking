from common.http import not_found, enable_cors, require_auth
from stats.data_source import read_stats, NoSuchUser, read_detailed_stats, NoSuchEntry
from common.firebase import init_firebase
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
    return read_stats(request.args.get['email'])
  except(NoSuchUser):
    not_found('No such user found')

@enable_cors
def get_detailed_stats(request):
  id = request.args.get('id')
  try:
    return read_detailed_stats(id)
  except(NoSuchEntry):
    not_found('No such entry found')