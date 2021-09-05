from werkzeug.exceptions import BadRequest, Unauthorized
from common.http import get_header, enable_cors, require_auth
from pytest import raises
from mock import Mock, patch

def test_can_get_header_case_insensitive():
  header = get_header({'lowercase': 'value'}, 'LOWERCASE')
  assert header == 'value'

def test_throws_key_error_if_not_found():
  with raises(KeyError, match="'missing'"):
    assert get_header({}, 'missing')

@enable_cors
def fake_wrapped_request_method(request):
  response_type = request.args['response']
  if response_type == 'text':
    return 'text'
  elif response_type == 'tuple':
    return ('tuple', 200)
  elif response_type == 'full_tuple':
    return ('full_tuple', 201, {'Header': 'value'})
  elif response_type == 'exception':
    raise BadRequest('Some error')

  raise Exception('no response type given')

def test_returns_headers_on_options():
  print('starting here')
  request = Mock(method='OPTIONS')
  print(f"method = {request.method}")
  assert request.method == 'OPTIONS'
  response = fake_wrapped_request_method(request)
  assert response == ('', 204, {
      'Access-Control-Allow-Origin': '*',
      'Access-Control-Allow-Methods': '*',
      'Access-Control-Allow-Headers': 'Content-Type, Authorization',
      'Access-Control-Max-Age': '3600'
  })

def test_adds_headers_to_simple_response():
  request = Mock(args={'response': 'text'}, method='GET')
  response = fake_wrapped_request_method(request)
  assert response == ('text', 200, {'Access-Control-Allow-Origin': '*'})

def test_adds_headers_to_response_tuple():
  request = Mock(args={'response': 'tuple'}, method='GET')
  response = fake_wrapped_request_method(request)
  assert response == ('tuple', 200, {'Access-Control-Allow-Origin': '*'})

def test_adds_headers_to_full_tuple():
  request = Mock(args={'response': 'full_tuple'}, method='GET')
  response = fake_wrapped_request_method(request)
  assert response == ('full_tuple', 201, {'Header': 'value', 'Access-Control-Allow-Origin': '*'})

def test_adds_headers_to_exception():
  request = Mock(args={'response': 'exception'}, method='GET')
  with raises(BadRequest):
    fake_wrapped_request_method(request)

@require_auth
def method_requiring_auth():
  pass

def test_get_stats_fails_without_token():
  request = Mock(headers={})
  with raises(Unauthorized, match=r'No Authorization header provided'):
    method_requiring_auth(request)

def test_get_stats_fails_with_bad_token():
  request = Mock(headers={'authorization': 'Bearer bob'})
  with raises(Unauthorized, match=r'Invalid token'):
    with patch('firebase_admin.auth.verify_id_token') as verify_mock:
      verify_mock.side_effect = Exception('Invalid token')
      method_requiring_auth(request)