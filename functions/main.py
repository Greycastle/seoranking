from register.register import register
from rank.rank import rank
from stats.stats import get_stats, get_detailed_stats
from processranking.processranking import process_ranking
from logresults.logresults import log_ranking_results
from addranking.addranking import handle_add_ranking_event, handle_add_ranking_request
from mailer.mailer import handle_send_mail_event
from notifyranking.notifyranking import notify_ranking

def register_http(request):
  return register(request)

def get_stats_http(request):
  return get_stats(request)

def get_detailed_stats_http(request):
  return get_detailed_stats(request)

def rank_message(event, context):
  rank(event, context)

def process_ranking_message(event, context):
  process_ranking(event, context)

def log_ranking_results_message(event, context):
  log_ranking_results(event, context)

def add_ranking_message(event, context):
  handle_add_ranking_event(event, context)

def add_ranking_http(request):
  return handle_add_ranking_request(request)

def send_mail_message(event, context):
  handle_send_mail_event(event, context)

def notify_ranking_message(event, context):
  notify_ranking(event, context)