# SEO Ranking

Tool to let people who can't afford huge tools like SEM Rush to get on track with their SEO ranking over time.

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

## Roadmap

- Localize the email
- Cache results for faster loading
- Make colour coding less horrible
- Add google login
- Add link to google result page
- Make share links better
- Add share buttons for good results
- Improve call to actions by splitting pages up
- Add slack integration