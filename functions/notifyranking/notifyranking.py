from common.publisher import publish
from common.events import get_event_data
from notifyranking.storage import get_last_ranking

def notify_ranking(event, context):
  data = get_event_data(event)
  site = data['rank_site']
  position = data['position']
  keyword = data['keyword']
  user = data['user']

  last_ranking = get_last_ranking(user, keyword, site)
  if last_ranking == position:
    print(f"Rank for site '{site}' on '{keyword}' is still ranking {position}, skipping email notification")
    return

  publish('send-mail', {
    'from': 'david@greycastle.se',
    'to': user,
    'subject': f'New ranking update for {site}',
    'html_content': build_email(last_ranking, position, site, keyword)
  })

def build_rank_change(prev_rank, new_rank):
  if prev_rank < 0:
    if new_rank < 0:
      return f"Your site ranking has been checked, but unfortunately, you don't rank within the first five result pages."
    else:
      return f"Your site ranking has been confirmed, you are ranking at position {prev_rank}"

  if new_rank < 0:
    return f"You previously ranked {prev_rank} but are no longer appearing within the first five result pages."

  return f"Your rank has changed from {prev_rank} to {new_rank}."

def build_email(last_ranking, ranking, site, keyword):

  rank_change_message = build_rank_change(last_ranking, ranking)
  return f"""
  Hi!
  <p>Your rank for {site} and keywords '{keyword}' was just updated.</p>

  <p>{rank_change_message}</p>

  <p>Check out your current and new rankings on the <a href="https://rank.greycastle.se/dashboard">History page</a>.</p>

  <p>If you wonder about anything, feel free to respond to this email, it goes straight to my inbox.</p>

  <p>See you next time!<br />
  Kind regards,<br/>
  David</p>
  """