# SEO Ranking

Tool to let people who can't afford huge tools like SEM Rush to get on track with their SEO ranking over time.

## Environment

As a development environment, you can load all your environment key secrets using a `source .env`.

## Functions

In the `functions` folder all cloud functions are stored.

To get started with running these locally you need to have [Python 3 installed](https://opensource.com/article/19/5/python-3-default-mac). Then you can debug locally using the [Functions Framework](https://cloud.google.com/functions/docs/running/function-frameworks).

```shell
pyenv exec pip install functions-framework
```

Then to run a specific function, cd into the directory and run the following, replacing it with the function name:

```shell
cd functions/helloworld
pyenv exec functions_framework --target hello_http
```

You can now call this method on [http://localhost:8080](http://localhost:8080).


### Dependencies

You add depenencies to the `requirements.txt` file however, first, check out the [pre-installed dependencies](https://cloud.google.com/functions/docs/writing/specifying-dependencies-python) documentation.