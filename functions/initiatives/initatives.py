from common.http import enable_cors, require_auth
from initiatives.data_source import get_initatives_for_user
from common.firebase import init_firebase

init_firebase()

@enable_cors
@require_auth
def get_initatives(request):
  items = get_initatives_for_user(request.user['email'])
  print(items)
  return { "items": items }