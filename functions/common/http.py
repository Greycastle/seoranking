from werkzeug.exceptions import BadRequest, HTTPException, NotFound, Unauthorized
from flask import Response
from functools import wraps
from firebase_admin import auth
import re

def not_found(message):
  raise NotFound(message)

def unauthorized(message):
  raise Unauthorized(message)

def bad_request(message):
  raise BadRequest(message)

def enable_cors(fn):
  @wraps(fn)
  def wrapped(request):
    if request.method == 'OPTIONS':
      headers = {
          'Access-Control-Allow-Origin': '*',
          'Access-Control-Allow-Methods': '*',
          'Access-Control-Allow-Headers': 'Content-Type, Authorization',
          'Access-Control-Max-Age': '3600'
      }
      return ('', 204, headers)

    cors_header = {'Access-Control-Allow-Origin': '*'}
    try:
      response = fn(request)
    except HTTPException as e:
      if e.response is None:
        e.response = Response(e.description, e.code, headers={})
      e.response.headers.update(cors_header)
      raise

    if type(response) == tuple:
      if len(response) == 2:
        return (response[0], response[1], cors_header)
      elif len(response) == 3:
        response[2].update(cors_header)
        return response

    return (response, 200, cors_header)

  return wrapped

def require_auth(fn):
  @wraps(fn)
  def wrapped(request):
    try:
      # Handle bearer prefix and case insensitive header
      auth_header = get_header(request.headers, 'Authorization')
      pattern  = re.compile("Bearer ", re.IGNORECASE)
      token = pattern.sub("", auth_header)
      request.user = auth.verify_id_token(token)
    except KeyError:
      unauthorized('No Authorization header provided')
    except Exception as e:
      unauthorized(f'{e}')

    return fn(request)

  return wrapped


def get_header(headers, header_name):
  for key in headers.keys():
    if key.lower() == header_name.lower():
      return headers[key]

  raise KeyError(header_name)