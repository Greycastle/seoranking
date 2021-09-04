from register.register import register
from rank.rank import rank

def register_http(request):
  return register(request)

def rank_message(event, context):
  rank(event, context)