# Artifice Scraper

[![Build Status](https://travis-ci.org/artifice-project/artifice-scraper.svg?branch=master)](https://travis-ci.org/artifice-project/artifice-scraper)
[![Maintainability](https://api.codeclimate.com/v1/badges/b6d2a8127db3dd42e77e/maintainability)](https://codeclimate.com/github/artifice-project/artifice-scraper/maintainability)
[![Python 3.6](https://img.shields.io/badge/python-3.6-blue.svg)](https://www.python.org/downloads/release/python-360/)
[![Python 3.7](https://img.shields.io/badge/python-3.7-blue.svg)](https://www.python.org/downloads/release/python-370/)
[![Python 3.8](https://img.shields.io/badge/python-3.8-blue.svg)](https://www.python.org/downloads/release/python-380/)
[![Python 3.9](https://img.shields.io/badge/python-3.9-blue.svg)](https://www.python.org/downloads/release/python-390/)

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

Start the Celery worker
```bash
artifice.scraper runcelery
```

Finally you can run the application:
```bash
artifice.scraper runserver
```

or play in the Python REPL:
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
