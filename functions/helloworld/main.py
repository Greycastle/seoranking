from flask import escape
from helloworld.google_search import search

def hello_http(request):
    query = request.args['query']
    return search(query)