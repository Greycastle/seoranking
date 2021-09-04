from common.publisher import publish
from common.events import get_event_data

def notify_ranking(event, context):
  data = get_event_data(event)

  site = data['rank_site']
  publish('send-mail', {
    'from': 'david@greycastle.se',
    'to': data['user'],
    'subject': f'New ranking update for {site}',
    'html_content': build_email(data['position'], site, data['keyword'])
  })

def build_email(ranking, site, keyword):
  return f"""
  Hi!
  Your rank for {site} and keywords '{keyword}' was just updated.

  You are now ranking on {ranking} place.

  Check out your current and new rankings on the <a href="https://rank.greycastle.se/history.html">History page</a>.

  If you wonder about anything, feel free to respond to this email, it goes straight to my inbox.

  See you next time!
  """