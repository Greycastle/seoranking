import mock
from datetime import datetime
from logresults.logresults import log_ranking_results
from common.testing import get_event_from_dict

def test_log_results():
  event = get_event_from_dict({
      'user': 'test@greycastle.se',
      'keyword': 'greycastle',
      'rank_site': 'greycastle.se',
      'timestamp': datetime.now().isoformat(),
      'position': 4
  })

  log_ranking_results(event, mock.Mock())

def test_log_results_with_details_id():
  event = get_event_from_dict({
      'user': 'test@greycastle.se',
      'keyword': 'greycastle',
      'rank_site': 'greycastle.se',
      'timestamp': datetime.now().isoformat(),
      'position': 4,
      'rankingDocPath': 'ranking/20210904_055621_600877'
  })

  log_ranking_results(event, mock.Mock())