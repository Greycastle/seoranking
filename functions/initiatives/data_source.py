from firebase_admin import firestore

def get_initatives_for_user(user_name):
  if user_name == None:
    raise Exception('User name is required')

  db = firestore.client()
  entries = db.collection('initatives').where('user', '==', user_name).stream()
  return list(map(lambda x: map_initative(x), entries))

def map_initative(initiative_doc):
  initative = initiative_doc.to_dict()
  return {
    'date': initative['date'].isoformat(),
    'description': initative['description'],
    'title': initative['title']
  }