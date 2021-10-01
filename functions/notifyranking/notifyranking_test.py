from notifyranking.notifyranking import notify_ranking, build_email
from common.testing import get_event_from_dict
from notifyranking.storage import get_last_ranking
from datetime import datetime
import mock

def test_notifies_on_new_ranking_if_no_previous():
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
    last_rank = get_last_ranking('test@greycastle.se', 'greycastle', 'greycastle.se')
    content = build_email(last_rank, 5, 'greycastle.se', 'greycastle', 'test@greycastle.se')
    mock_publish.assert_called_once_with('send-mail', {
      'to': 'test@greycastle.se',
      'from': 'david@greycastle.se',
      'subject': "New ranking update for greycastle.se",
      'html_content': content
    })