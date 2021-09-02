import datetime
from inspect import unwrap

from werkzeug.exceptions import BadRequest, Unauthorized
import firebase_admin
from firebase_admin import auth
from firebase_admin import credentials
import os
from flask import abort, Response
from data_source import read_stats, NoSuchUser
import re
import logging

logger = logging.getLogger(__name__)

PROJECT_ID = os.getenv('GCP_PROJECT')
cred = credentials.ApplicationDefault()
firebase_app = firebase_admin.initialize_app(cred, {
  'projectId': PROJECT_ID,
})

def unauthorized(message, headers):
  raise Unauthorized(message, Response(message, 401, headers=headers))

def bad_request(message, headers):
  raise BadRequest(message, Response(message, 400, headers=headers))

def get_stats(request):
  if request.method == 'OPTIONS':
    headers = {
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': 'GET',
            'Access-Control-Allow-Headers': 'Content-Type',
            'Access-Control-Max-Age': '3600'
        }
    return ('', 204, headers)

  headers = { 'Access-Control-Allow-Origin': '*' }
  if not request.headers.get('authorization'):
      unauthorized('No authorization token provided', headers)
  try:
      pattern  = re.compile("Bearer ", re.IGNORECASE)
      token = pattern.sub("", request.headers['authorization'])
      request.user = auth.verify_id_token(token)
  except Exception as e:
      logger.error("Invalid auth token", exc_info=e)
      bad_request('Invalid authorization token', headers)

  try:
    data = read_stats(request.user['email'])
    return (data, 200, headers)
  except(NoSuchUser):
    abort(404, 'No user found')