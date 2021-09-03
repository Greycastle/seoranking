from publisher import publish
from storage import get_rankings
from datetime import datetime

def process_ranking(event, context):
  rankings = get_rankings()
  print(f"Found {len(rankings)} rankings")

  next = find_next_ranking(rankings)
  if next is None:
    print("No pending ranking found, skipping.")
    return

  publish('rank', {
    'user': next['user'],
    'rank_site': next['rank_site'],
    'keyword': next['keyword'],
  })

def find_next_ranking(rankings):
  if len(rankings) == 0:
    return None

  sorted = list(rankings)
  sorted.sort(key=(lambda x: x['last_ranked'] or datetime(1, 1, 1)))
  return sorted[0]