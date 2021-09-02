from unittest import mock
from main import get_stats
from pytest import raises
from werkzeug import exceptions
import json

def test_get_stats_fails_without_token():
  request = mock.Mock(headers={})
  with raises(exceptions.Unauthorized, match=r'No authorization token provided'):
    get_stats(request)

def test_get_stats_fails_with_bad_token():
  request = mock.Mock(headers={'authorization': 'Bearer bob'})
  with raises(exceptions.BadRequest, match=r'Invalid authorization token'):
    get_stats(request)

def test_get_stats():

  request = mock.Mock(headers={'authorization': 'jwt'})
  mock_user = {
    'email': 'david@greycastle.se'
  }
  with mock.patch('firebase_admin.auth.verify_id_token') as verify_mock:
    verify_mock.return_value = mock_user
    get_stats(request)