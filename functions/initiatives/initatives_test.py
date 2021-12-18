from initiatives.initatives import get_initatives
from unittest import mock

def test_get_initatives():
  request = mock.Mock(headers={'authorization': 'Bearer mock-token'}, method='GET')
  mock_user = {
    'email': 'ddikman@gmail.com'
  }
  with mock.patch('firebase_admin.auth.verify_id_token') as verify_mock:
    verify_mock.return_value = mock_user
    response, status, _ = get_initatives(request)
    assert status == 200

    number_of_items = len(response["items"])
    assert number_of_items > 0

    an_item = response["items"][0]
    assert an_item.keys() == {'title', 'date', 'description'}