from unittest import mock
from stats.stats import get_stats, get_detailed_stats
from stats.data_source import encode_id

def test_get_stats():
  request = mock.Mock(headers={'authorization': 'Bearer mock-token'}, method='GET')
  mock_user = {
    'email': 'david@greycastle.se'
  }
  with mock.patch('firebase_admin.auth.verify_id_token') as verify_mock:
    verify_mock.return_value = mock_user
    get_stats(request)
    verify_mock.assert_called_once_with('mock-token')


def test_can_get_details():
  args = {
    'id': encode_id('flutter greycastle', 'greycastle.se', 'test@greycastle.se')
  }
  request = mock.Mock(method='GET', args=args)
  response = get_detailed_stats(request)
  assert len(response) > 0