import mock
from datetime import datetime
import base64
import json
from logresults.logresults import log_ranking_results

def test_log_results():
  event = {
    'data': base64.b64encode(json.dumps({
      'user': 'test@greycastle.se',
      'keyword': 'greycastle',
      'rank_site': 'greycastle.se',
      'timestamp': datetime.now().isoformat(),
      'position': 4
    }).encode()).decode()
  }

  log_ranking_results(event, mock.Mock())
