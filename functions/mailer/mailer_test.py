from common.testing import get_event_from_dict
from mailer.mailer import handle_send_mail_event
from mock import Mock

def test_can_send_mail():
  event = get_event_from_dict({
    'from': "david@greycastle.se",
    "to": "ddikman@gmail.com",
    "subject": "Integration test email",
    "html_content": '<a href="https://seorank.app/">Check the site out</a>'
  })

  handle_send_mail_event(event, Mock())