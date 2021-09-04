from register.register import register
from rank.rank import rank
from stats.stats import get_stats

def register_http(request):
  return register(request)

def rank_message(event, context):
  rank(event, context)

def get_stats_http(request):
  get_stats(request)