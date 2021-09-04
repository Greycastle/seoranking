from flask import abort, Response
import validators
from storage import register_new_user, UserAlreadyAdded
from werkzeug.exceptions import BadRequest

def bad_request(message, headers):
  raise BadRequest(message, Response(message, 400, headers=headers))

def register(request):
    if request.method == 'OPTIONS':
      headers = {
              'Access-Control-Allow-Origin': '*',
              'Access-Control-Allow-Methods': 'POST, OPTION',
              'Access-Control-Allow-Headers': 'Content-Type, Authorization',
              'Access-Control-Max-Age': '3600'
          }
      return ('', 204, headers)

    headers = { 'Access-Control-Allow-Origin': '*' }

    query = request.args.get('query')
    rank_site = request.args.get('rank_site')
    user = request.args.get('user')

    if not user or not query or not rank_site:
      bad_request('query, rank_site and user must be specified', headers)

    if not validators.domain(rank_site):
      bad_request(f'rank_site is not a valid domain: {rank_site}', headers)

    if not validators.email(user):
      bad_request(f'user is not a valid email: {user}', headers)

    try:
      register_new_user(username=user, keyword=query, rank_site=rank_site)
      return ('ok', 200, headers)
    except UserAlreadyAdded:
      return ('already added', 200, headers)
