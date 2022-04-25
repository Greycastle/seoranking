def bill_user(db, user):
  user_doc = next(db.collection('users').where('email', '==', user).stream(), None)
  data = user_doc.to_dict()
  ranks_used = data.get('ranks_used', 0) + 1
  ranks_left = data.get('ranks_left', 0) - 1
  user_doc.reference.update({
    'ranks_left': ranks_left,
    'ranks_used': ranks_used
  })
  print(f"Billed {user} one credit, {ranks_left} credits remaining")

def log_latest_result(db, user, keyword, rank_site, rank, timestamp, rankingDocPath):
  user_doc = next(db.collection('users').where('email', '==', user).stream(), None)
  data = user_doc.to_dict()

  all_rankings = data.get('rankings', None)
  if all_rankings is None:
    raise NoSuchRanking

  ranking = next(filter(lambda x: x['site'] == rank_site and x['keyword'] == keyword, all_rankings), None)
  if ranking is None:
    raise NoSuchRanking

  if rankingDocPath is not None:
    ranking['last_ranking_path'] = rankingDocPath

  ranking['last_position'] = rank
  ranking['last_ranked'] = timestamp

  user_doc.reference.update({
    'rankings': all_rankings
  })
  print(f"Updated site {rank_site} ranking for '{keyword}' to position: {rank}")

class NoSuchRanking(Exception):
  pass