from flask import Response
import validators
from register.storage import register_new_user, UserAlreadyAdded
from common.publisher import publish
from common.http import enable_cors, bad_request

@enable_cors
def register(request):
    query = request.args.get('query')
    rank_site = request.args.get('rank_site')
    user = request.args.get('user')

    if not user or not query or not rank_site:
      bad_request('query, rank_site and user must be specified')

    if not validators.domain(rank_site):
      bad_request(f'rank_site is not a valid domain: {rank_site}')

    if not validators.email(user):
      bad_request(f'user is not a valid email: {user}')

    try:
      register_new_user(user)
      publish('add-ranking', {
        'user': user,
        'rank_site': rank_site,
        'keyword': query
      })
      print(f'Requested ranking for {rank_site} to be added')
      return 'ok'
    except UserAlreadyAdded:
      return 'already added'
