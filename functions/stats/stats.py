
from common.http import bad_request, not_found, enable_cors, require_auth
from stats.data_source import read_stats, NoSuchUser
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