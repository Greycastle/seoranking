from google.cloud import pubsub_v1
import os
import json

def publish(topic_name, message):
  publisher = pubsub_v1.PublisherClient()
  PROJECT_ID = os.getenv('GCP_PROJECT')

  if not topic_name or not message:
    raise Exception("Must supply topic_name and message to publish")

  message_json = json.dumps(message)
  message_bytes = message_json.encode('utf-8')

  topic_path = publisher.topic_path(PROJECT_ID, topic_name)
  publish_future = publisher.publish(topic_path, data=message_bytes)
  publish_future.result()