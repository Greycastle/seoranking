import requests
from bs4 import BeautifulSoup

def run_search(query, stop_on):
  query = query.replace(' ', '+').lower()
  human_language = "ja"
  geo_location = "jp"
  first_page_url = f"https://www.google.com/search?q={query}&hl={human_language}&gl={geo_location}"

  resp = get_url(first_page_url)
  if resp.status_code == 200:
    return parse_page(
      content=resp.content,
      stop_on=stop_on
    )
  else:
    raise Exception(f"Failed to parse with response {resp.status_code}")


def parse_page(content, stop_on, pages_left = 5):
    soup = BeautifulSoup(content, "html.parser")
    results = []
    found = []
    matches = soup.select('div.g')
    for match in matches:
        link = match.select('a')[0]
        link_id = link['data-ved']
        # skip previous match
        if link_id in found:
          continue

        found.append(link_id)
        title = link.select('h3')[0]
        results.append({
          'link': link['href'].lower(),
          'title': title.text
        })

    if is_match(stop_on, results):
      print(f"found stop domain {stop_on} with {pages_left} pages left to scrape")
      return results

    if (pages_left == 0):
      return results

    navigation = soup.select("div[role='navigation'] a")
    if len(navigation) == 0:
      return results

    next_page_url = "https://www.google.com" + navigation[-1]['href']
    # print(f"got next page: {next_page_url}")
    next_page = get_url(next_page_url)
    if next_page.status_code != 200:
      print(f"Got [{next_page.status_code}] for url {next_page_url}, aborting")
      return results

    next_page_results = parse_page(content=next_page.content, stop_on=stop_on, pages_left=pages_left - 1)
    return results + next_page_results

def is_match(find_site, sites):
  for site in sites:
    if find_site in site['link']:
      return True

  return False

def get_url(url):
  USER_AGENT = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:65.0) Gecko/20100101 Firefox/65.0"
  headers = {"user-agent" : USER_AGENT}
  print(f"scraping url: {url}")
  return requests.get(url, headers=headers)
