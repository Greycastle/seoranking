from werkzeug.exceptions import BadRequest, Unauthorized
from flask import Response

def unauthorized(message, headers):
  raise Unauthorized(message, Response(message, 401, headers=headers))

def bad_request(message, headers):
  raise BadRequest(message, Response(message, 400, headers=headers))
