from unittest import mock
from stats.stats import get_stats, get_detailed_stats, get_public_stats
from common.ranking_id import encode_id
import base64

def test_get_stats():
  request = mock.Mock(headers={'authorization': 'Bearer mock-token'}, method='GET')
  mock_user = {
    'email': 'david@greycastle.se'
  }
  with mock.patch('firebase_admin.auth.verify_id_token') as verify_mock:
    verify_mock.return_value = mock_user
    get_stats(request)
    verify_mock.assert_called_once_with('mock-token')

def test_get_public_stats():
  id = base64.b64encode("david@greycastle.se".encode()).decode()
  request = mock.Mock(args={'id': id}, method='GET')
  (response, status, _) = get_public_stats(request)
  assert status == 200
  assert list(response.keys()) == [ 'items' ]
  assert len(response['items']) > 0

def test_can_get_details():
  args = {
    'id': encode_id('flutter greycastle', 'greycastle.se', 'test@greycastle.se')
  }
  request = mock.Mock(method='GET', args=args)
  (response, status, _) = get_detailed_stats(request)
  assert status == 200
  assert len(response) > 0

  stats_sample = response['stats'][0]
  assert type(stats_sample['date']) == str
  assert type(stats_sample['rank']) == int