from addranking.addranking import add_ranking
from common.testing import get_event_from_dict
import mock

def test_skips_existing_ranking():
  event = get_event_from_dict({
    'user': 'test@greycastle.se',
    'rank_site': 'greycastle.se',
    'keyword': 'greycastle',
  })

  with mock.patch('addranking.addranking.publish') as publish_mock:
    add_ranking(event, mock.Mock())
    publish_mock.assert_not_called()

def test_triggers_ranking_after_adding():
  event_data = {
    'user': 'test@greycastle.se',
    'rank_site': 'greycastle.se',
    'keyword': 'greycastle',
  }
  event = get_event_from_dict(event_data)

  with mock.patch('addranking.addranking.save_ranking') as save_mock:
    save_mock.return_value = None
    with mock.patch('addranking.addranking.publish') as publish_mock:
      add_ranking(event, mock.Mock())
      publish_mock.assert_called_once_with('rank', event_data)