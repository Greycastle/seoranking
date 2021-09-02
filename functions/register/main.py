from flask import abort
import validators
from storage import register_new_user, UserAlreadyAdded

def register(request):
    query = request.args.get('query')
    rank_site = request.args.get('rank_site')
    user = request.args.get('user')

    if not user or not query or not rank_site:
      abort(400, 'query, rank_site and user must be specified')

    if not validators.domain(rank_site):
      abort(400, f'rank_site is not a valid domain: {rank_site}')

    if not validators.email(user):
      abort(400, f'user is not a valid email: {user}')

    try:
      register_new_user(username=user, keyword=query, rank_site=rank_site)
      return 'ok'
    except UserAlreadyAdded:
      return 'already added'
