# Artifice Scraper

[![Build Status](https://travis-ci.org/minelminel/flask-boilerplate.svg?branch=master)](https://travis-ci.org/minelminel/flask-boilerplate)

## Installation

First, clone the repository and create a virtualenv. Then install the requirements:

`$ pip install -e .`

Before running the application make sure that your local PostgreSQL server is up. Then create the databases:

```sql
CREATE DATABASE artifice_scraper;
CREATE DATABASE artifice_scraper_test;
```

Now you can create the tables using Alembic:
```bash
artifice.scraper db init
artifice.scraper db migrate
artifice.scraper db upgrade
```

Finally you can run the application:
```bash
artifice.scraper runserver
```

or play in the Python REPL:
```bash
artifice.scraper shell
```

In order to run unit tests in py.test invoke:
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

TODO:
- ~~Connect supervisor object to current_app.config object, rather than a pure object state~~
- User request body args for content and queue GET requests, rather than url params
- Copy in utils
- Copy in schemas
- Copy in tasks
- Inside tasks, use env var to store the loopback url for content, status, queue, etc
- start celery with current app config
- Copy in models
- Check imports
- Copy in resources
- Disable redis for Now
- Check endpoints
- Post to status
