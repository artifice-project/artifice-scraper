# Artifice Scraper :scissors:

[![Build Status](https://travis-ci.org/artifice-project/artifice-scraper.svg?branch=master)](https://travis-ci.org/artifice-project/artifice-scraper)
[![Maintainability](https://api.codeclimate.com/v1/badges/b6d2a8127db3dd42e77e/maintainability)](https://codeclimate.com/github/artifice-project/artifice-scraper/maintainability)
[![codecov](https://codecov.io/gh/artifice-project/artifice-scraper/branch/master/graph/badge.svg)](https://codecov.io/gh/artifice-project/artifice-scraper)
[![PyPI license](https://img.shields.io/pypi/l/ansicolortags.svg)](https://pypi.python.org/pypi/ansicolortags/)
[![Deployment](https://img.shields.io/badge/deployment-ansible-blueviolet)](https://shields.io/)
[![Python 3.6](https://img.shields.io/badge/python-3.6-blue.svg)](https://www.python.org/downloads/release/python-360/)
[![Python 3.7](https://img.shields.io/badge/python-3.7-blue.svg)](https://www.python.org/downloads/release/python-370/)
<!-- [![Python 3.8](https://img.shields.io/badge/python-3.8-blue.svg)](https://www.python.org/downloads/release/python-380/) -->
<!-- [![Python 3.9](https://img.shields.io/badge/python-3.9-blue.svg)](https://www.python.org/downloads/release/python-390/) -->

## Installation

```bash
git clone https://github.com/artifice-project/artifice-scraper.git
cd artifice-scraper
virtualenv env && source env/bin/activate
pip install .
```

Before running the application make sure that your local PostgreSQL server is up. To create and initialize the database, use the Makefile:
```bash
make database
```

Start the Celery worker
```bash
artifice.scraper runcelery
```

Finally you can run the application:
```bash
artifice.scraper runserver
# by default, runs at port 5000
```

The default config file can be overridden either by specifying an environment variable, or with a command line option:
```bash
# envvar
export FLASK_CONFIG_PATH=/path/to/config
# cli option
artifice.scraper -c ../config/local.py    # development (DEFAULT)
artifice.scraper -c ../config/staging.py  # production
artifice.scraper -c ../config/testing.py  # testing
```

To run the Python REPL:
```bash
artifice.scraper shell
```

In order to run unit tests with app context, invoke:
```bash
artifice.scraper test
```

To view test coverage:
```bash
artifice.scraper coverage
```

There is a preconfigured WSGI module located at `artifice.scraper.core.wsgi`. Example usage with Gunicorn:
```bash
gunicorn --workers 1 --bind 0.0.0.0:8000 artifice.scraper.core.wsgi:application
```

If the process fails to start, try prepending the `gunicorn` with its relative path within your virtual environment, for example `env/bin/gunicorn ...`


## Usage

The application has two main parts: an api, and asynchronous task queue. A general overview of the control flow is outlined below.

![Artifice-Scraper](https://user-images.githubusercontent.com/46664545/64927264-883a3500-d7d6-11e9-83ed-06dc7eb7276f.png)

To begin scraping, first ensure that the Supervisor is enabled. This can be done either by specifying default config values, or by sending a request to the `/status` endpoint. Below is an example of a request which accomplishes this task.

`POST` `/status`
```json
/* REQUEST */
{
  "enabled": true,
  "debug": false
}
```

Now that the service is active, we can provide a seed url. This url will be used to filter all links extracted from the page, ensuring that the scraper remains focused on the specified website and does not accidentally venture out into the web via an advertisement or external link.

`POST` `/queue`
```json
/* REQUEST */
{
  "url": "https://www.npr.org/sections/politics"
}
```
Multiple seeds can also be specified by providing a list.
```json
/* REQUEST */
{
  "url": [
    "https://www.npr.org/sections/politics",
    "https://www.npr.org/sections/business"
  ]
}
```

To monitor database sizes, utilize the `/metrics` endpoint.

`GET` `/metrics`
```json
/* RESPONSE */
{
  "content": {
    "total": 0
  },
  "queue": {
    "DONE": 0,
    "READY": 0,
    "TASKED": 0,
    "total": 0
  }
}
```

To monitor the queue, utilize the `/queue` endpoint.

`GET` `/queue`
```json
/* REQUEST */
{
  "limit": 10,
  "status": [
    "TASKED"
  ]
}

/* RESPONSE */
{
  "msg": {
    "limit": 10,
    "status": [
      "TASKED"
    ]
  },
  "reply": [
    {
      "created_at": "2019-09-15T01:05:35.201115+00:00",
      "id": 1,
      "modified_at": null,
      "status": "TASKED",
      "url": "https://www.npr.org/sections/politics"
    },
    {
      "created_at": "2019-09-15T01:05:35.201115+00:00",
      "id": 2,
      "modified_at": null,
      "status": "TASKED",
      "url": "https://www.npr.org/sections/business"
    }
  ]
}
```

To view the scraped content, utilize the `/content` endpoint. Query parameters can be specified within the request body.

`GET` `/content`
```json
/* BODY */
{
  "limit": 10
}

/* RESPONSE */
{
  "msg": {
    "limit": 10
  },
  "reply": [
    {
      "created_at": "2019-09-15T01:05:35.201115+00:00",
      "id": 1,
      "modified_at": null,
      "origin": "https://www.npr.org/sections/politics",
      "title": "Politics : NPR",
      "captions": ["Firefighters battle the blaze as fires continue to spread across Southern California [Credit: Reuters]"],
      "text": "5 Questions Answered About The 3rd Democratic Debate \
      Latinx Advocacy Groups Sue To Block Citizenship Data Release By Trump Officials \
      'I Wasn't Naive': Getting Fired In The Trump Administration"
    }
  ]
}
```

To temporarily disable the service from scraping, utilize the `/status` endpoint. Urls from the task queue will be sent back to the api with a status designation of `READY`, meaning they can easily be re-dispatched once the service is enabled again.

`POST` `/status`
```json
/* REQUEST */
{
  "enabled": false
}
```
**Note: it may take some time for the system to empty the entire task queue, as it may have become arbitrarily large during operation. Monitor the `/metrics` endpoint and wait for the number of `TASKED` items to stop increasing.**

To reenable the service and continue scraping, first utilize the `/status` endpoint to specify the state as enabled.
`POST` `/status`
```json
/* REQUEST */
{
  "enabled": true
}
```
Then, you can release the `READY` items to the queue by utilizing the same endpoint with an empty `PUT` request. Verify success by monitoring the `/queue` endpoint and ensuring the number of `READY` items is decreasing as `TASKED` increases.
