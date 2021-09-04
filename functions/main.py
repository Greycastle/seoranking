from register.register import register
from rank.rank import rank
from stats.stats import get_stats
from processranking.processranking import process_ranking

def register_http(request):
  return register(request)

def rank_message(event, context):
  rank(event, context)

def get_stats_http(request):
  get_stats(request)

def process_ranking_message(event, context):
  process_ranking(event, context)