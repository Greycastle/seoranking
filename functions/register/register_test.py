from main import register
from unittest.mock import Mock
from pytest import raises
from werkzeug import exceptions

def test_endpoint_invalid_input():
  request = Mock(args={'user': 'username'})
  with raises(exceptions.BadRequest):
    assert register(request)

def test_site_is_url():
  request = Mock(args={'user': 'username', 'query': 'kw', 'rank_site': 'not url'})
  with raises(exceptions.BadRequest, match=r'rank_site'):
    assert register(request)

def test_username_is_email():
  request = Mock(args={'user': 'username', 'query': 'kw', 'rank_site': 'site.com'})
  with raises(exceptions.BadRequest, match=r'user'):
    assert register(request)

def test_can_register():
  request = Mock(args={
    'user': 'test@greycastle.se',
    'query': 'greycastle',
    'rank_site': 'greycastle.se'
  })
  response = register(request)
  assert response == 'already added'