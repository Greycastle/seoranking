from notifyranking.notifyranking import notify_ranking, build_email
from common.testing import get_event_from_dict
from datetime import datetime
import mock

def test_notifies_on_new_ranking():
  event = get_event_from_dict({
    'user': 'test@greycastle.se',
    'keyword': 'greycastle',
    'rank_site': 'greycastle.se',
    'timestamp': datetime.now().isoformat(),
    'position': 5,
    'results': []
  })

  with mock.patch('notifyranking.notifyranking.publish') as mock_publish:
    notify_ranking(event, mock.Mock())
    content = build_email(5, 'greycastle.se', 'greycastle')
    mock_publish.assert_called_once_with('send-mail', {
      'to': 'test@greycastle.se',
      'from': 'david@greycastle.se',
      'subject': "New ranking update for greycastle.se",
      'html_content': content
    })