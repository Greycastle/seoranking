from addranking.addranking import handle_add_ranking_event, handle_add_ranking_request
from common.testing import get_event_from_dict
import mock

def test_skips_existing_ranking():
  event = get_event_from_dict({
    'user': 'test@greycastle.se',
    'rank_site': 'greycastle.se',
    'keyword': 'greycastle',
  })

  with mock.patch('addranking.addranking.publish') as publish_mock:
    handle_add_ranking_event(event, mock.Mock())
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
      handle_add_ranking_event(event, mock.Mock())
      publish_mock.assert_called_once_with('rank', event_data)

def test_can_handle_http():
  request = mock.Mock(headers={'authorization': 'Bearer mock-token'}, method='GET')
  mock_user = {
    'email': 'david@greycastle.se'
  }
  request.get_json.return_value = { 'keyword': 'greycastle', 'rank_site': 'greycastle.se' }
  with mock.patch('firebase_admin.auth.verify_id_token') as verify_mock:
    verify_mock.return_value = mock_user
    response = handle_add_ranking_request(request)
    assert response[0] == 'ok'