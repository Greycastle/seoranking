from common.publisher import publish
from common.events import get_event_data
from notifyranking.storage import get_last_ranking

def notify_ranking(event, context):
  data = get_event_data(event)
  site = data['rank_site']
  position = data['position']
  keyword = data['keyword']
  user = data['user']

  if not rank_changed(user, site, keyword, position):
    print(f"Rank for site '{site}' on '{keyword}' is still ranking {position}, skipping email notification")
    return

  publish('send-mail', {
    'from': 'david@greycastle.se',
    'to': user,
    'subject': f'New ranking update for {site}',
    'html_content': build_email(position, site, keyword)
  })

def rank_changed(user, site, keyword, position):
  last_ranking = get_last_ranking(user, keyword, site)
  return last_ranking != position

def build_email(ranking, site, keyword):
  return f"""
  Hi!
  <p>Your rank for {site} and keywords '{keyword}' was just updated.</p>

  <p>You are now ranking on {ranking} place.</p>

  <p>Check out your current and new rankings on the <a href="https://rank.greycastle.se/history.html">History page</a>.</p>

  <p>If you wonder about anything, feel free to respond to this email, it goes straight to my inbox.</p>

  <p>See you next time!<br />
  Kind regards,<br/>
  David</p>
  """