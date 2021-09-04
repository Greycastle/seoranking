import sendgrid
from sendgrid.helpers.mail import *
from common.events import get_event_data
import os

def handle_send_mail_event(event, context):
  data = get_event_data(event)
  send_mail(data['from'], data['to'], data['subject'], data['html_content'])

def send_mail(from_email, to_email, subject, html_content):
  sg = sendgrid.SendGridAPIClient(api_key=os.environ.get('SENDGRID_KEY'))
  from_email = Email(from_email)
  to_email = To(to_email)
  content = Content("text/html", html_content)
  mail = Mail(from_email, to_email, subject, content)
  response = sg.client.mail.send.post(request_body=mail.get())
  if response.status_code != 202:
    raise MailSendFailed(f"Failed to send email [{response.status_code}]: {response.body}")

  print(f"Successfully sent email from {from_email} with subject line '{subject}'")

class MailSendFailed(Exception):
      def __init__(self, message):
        super().__init__(message)