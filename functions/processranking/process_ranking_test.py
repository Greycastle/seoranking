import datetime
import mock
from processranking.processranking import process_ranking, find_next_ranking

def get_datetime(hours_diff=0):
  return datetime.datetime.now() + datetime.timedelta(hours=hours_diff)

def test_skips_if_none_found():
  with mock.patch('processranking.processranking.get_rankings') as get_rankings_mock:
    get_rankings_mock.return_value = []
    with mock.patch('processranking.processranking.publish') as publish_mock:
      process_ranking({}, mock.Mock())
      publish_mock.assert_not_called()

def test_publishes_next_waiting():
  with mock.patch('processranking.processranking.get_rankings') as get_rankings_mock:
    expected = {
      'user': 'david@greycastle.se',
      'rank_site': 'greycastle.se',
      'keyword': 'greycastle',
      'last_ranked': get_datetime(hours_diff=-4)
    }
    get_rankings_mock.return_value = [ expected ]
    with mock.patch('processranking.processranking.publish') as publish_mock:
      process_ranking({}, mock.Mock())
      expected.pop('last_ranked')
      publish_mock.assert_called_once_with('rank', expected)


def test_picks_oldest_pending():
  expected = {
    'user': 'david@greycastle.se',
    'rank_site': 'greycastle.se',
    'keyword': 'greycastle',
    'last_ranked': get_datetime(hours_diff=-4)
  }
  rankings = [
    { 'rank_site': 'decoy_one.com', 'last_ranked': get_datetime(hours_diff=-2) },
    expected,
    { 'rank_site': 'decoy_two.com', 'last_ranked': get_datetime(hours_diff=-1) },
  ]
  result = find_next_ranking(rankings)
  assert result['rank_site'] == expected['rank_site']

def test_last_rank_missing_equals_not_yet_ranks():
  other = {
    'rank_site': 'other.se',
    'last_ranked': get_datetime()
  }
  expected = {
    'rank_site': 'expected.se',
    'last_ranked': None
  }
  result = find_next_ranking([other, expected, other])
  assert result['rank_site'] == expected['rank_site']