def bill_user(db, user):
  user_doc = next(db.collection('users').where('email', '==', user).stream(), None)
  data = user_doc.to_dict()
  ranks_used = data.get('ranks_used', 0) + 1
  ranks_left = data.get('ranks_left', 0) - 1
  user_doc.reference.update({
    'ranks_left': ranks_left,
    'ranks_used': ranks_used
  })

def log_latest_result(db, user, keyword, rank_site, rank, timestamp):
  user_doc = next(db.collection('users').where('email', '==', user).stream(), None)
  data = user_doc.to_dict()

  all_rankings = data.get('rankings', None)
  if all_rankings is None:
    raise NoSuchRanking

  ranking = next(filter(lambda x: x['site'] == rank_site and x['keyword'] == keyword, all_rankings), None)
  if ranking is None:
    raise NoSuchRanking

  ranking['last_position'] = rank
  ranking['last_ranked'] = timestamp

  user_doc.reference.update({
    'rankings': all_rankings
  })

class NoSuchRanking(Exception):
  pass