from unittest import mock
from stats.stats import get_stats

def test_get_stats():
  request = mock.Mock(headers={'authorization': 'Bearer mock-token'}, method='GET')
  mock_user = {
    'email': 'david@greycastle.se'
  }
  with mock.patch('firebase_admin.auth.verify_id_token') as verify_mock:
    verify_mock.return_value = mock_user
    get_stats(request)
    verify_mock.assert_called_once_with('mock-token')