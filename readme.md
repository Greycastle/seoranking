# SEO Ranking [Archived]

Tool to let people who can't afford huge tools like SEM Rush to get on track with their SEO ranking over time.

**Archive notice:**
This used to be hosted on https://myrank.se/ but it never really got off to any kind of start so July 30th, 2025, I decided to archive it to avoid paying for the domain.

<img width="1279" height="1079" alt="image" src="https://github.com/user-attachments/assets/3efd27db-f455-47bc-bab0-efcd5ae82cf1" />


## Environment

As a development environment, you can load all your environment key secrets using a `source .env`.

## Site

```
cd site-vue
npm install
npm run serve
```

## Functions

In the `functions` folder all cloud functions are stored.

To get started with running these locally you need to have [Python 3 installed](https://opensource.com/article/19/5/python-3-default-mac). Then you can debug locally using the [Functions Framework](https://cloud.google.com/functions/docs/running/function-frameworks).

```shell
pip install functions-framework
```

Then to run a specific function, cd into the directory and run the following, replacing it with the function name:

```shell
cd functions
functions_framework --target register_http
```

You can now call this method on [http://localhost:8080](http://localhost:8080).


### Dependencies

You add depenencies to the `requirements.txt` file. Check out the [pre-installed dependencies](https://cloud.google.com/functions/docs/writing/specifying-dependencies-python) documentation.

Even though the requirement might be available, add it to make local development easier.

You can then install these by:

```shell
pyenv exec pip install -r requirements.txt
```

### Testing

I use [pytest](https://docs.pytest.org/) for running unit tests. This helps iterate a bit more quickly for anything that's not specifically relying on the infrastructure part of running the functions.

Run it by

```shell
# making sure you are on the right firebase project
gcloud config set project seoranking-324303
export GCP_PROJECT=seoranking-324303
pytest
```

This will run all tests in the folder though, so you may want to filter out only specific tests for the function you are testing, for example:

```shell
pytest rank/*
```

To test publishers and similar you need to allow Google to give permissions to use your account to authenticate to stuff like pubsub.

```shell
gcloud auth application-default login
```

### Deploy

```shell
cd functions
./deploy.sh
```

## About google ranking

Google has a [Programmable Search Engine](https://developers.google.com/custom-search/v1/introduction) API but it works as a custom engine for your own site, not as an API for the site in general.

[SerpApi](https://serpapi.com/) is one service that scrapes Google and they take the blame for this. [Google hasn't taken any legal actions](https://dataforseo.com/blog/is-scraping-google-serps-legal) for companies scraping them but it is against their ToS.

Scraping google like this will sooner or later hit their rate limit and start returning 429 Too many requests. To avoid this but still keep cost down, when this happens, I fall back and use [https://scrape.do/](https://scrape.do/) as a proxy. As an improvement, I could add an exponential falloff or so until when I go back and use my own service but for now, I'll just try scraping on my own first and if it fails, fall back to using the proxy.

## Roadmap

- Add choice of country/language to run the query in
- Localize the email
- Cache results for faster loading
- Make colour coding less horrible
- Add google login
- Add link to google result page
- Make share links better
- Add share buttons for good results
- Improve call to actions by splitting pages up
- Add slack integration
- Add link to [google search trends](https://trends.google.com/trends/explore) for keywords


### Currently going on

Last edit I added `rankingDocPath` to the rankings for each user, the idea is to use this in `get_stats` to not have to iterate over all of the rankings to get the latest stats.

I also want to:
1. Keep a separate list of ranking positions
  - Potentially, I could move the rank results to a sub-collection instead
2. Save the number of rankings in `log_ranking_results` to not have to count them each time
