from google_search import run_search

# test by:
# curl "http://localhost:8080?query=greycastle&rank_site=greycastle.se"

def search(request):
    query = request.args['query']
    rank_site = request.args['rank_site']
    response = run_search(query=query, stop_on=rank_site)
    return {
      'items': response
    }