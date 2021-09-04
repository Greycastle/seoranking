from register.register import register
from rank.rank import rank
from stats.stats import get_stats
from processranking.processranking import process_ranking
from logresults.logresults import log_ranking_results

def register_http(request):
  return register(request)

def get_stats_http(request):
  return get_stats(request)

def rank_message(event, context):
  rank(event, context)

def process_ranking_message(event, context):
  process_ranking(event, context)

def log_ranking_results_message(event, context):
  log_ranking_results(event, context)