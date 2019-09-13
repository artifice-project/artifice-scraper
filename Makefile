# https://krzysztofzuraw.com/blog/2016/makefiles-in-python-projects.html
.PHONY: clean-pyc clean-build
HOST=127.0.0.1
TEST_PATH=./
PACKAGE=Artifice

clean-pyc:
	@echo "	clean-pyc"
	@echo "		Remove python artifacts"
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +

clean-build:
	@echo "	clean-build"
	@echo "		Remove build artifacts."
	rm -rf build/
	rm -rf dist/
	rm -rf *.egg-info

build:
	@echo "	build"
	@echo "		Build source distribution & wheel"
	python3 setup.py sdist bdist_wheel

db-reset:
	@echo "	db-reset"
	@echo "		Drop current database(s) and reset migrations"
	rm -rf migrations/
	psql -c "DROP DATABASE artifice_scraper";
	psql -c "DROP DATABASE artifice_scraper_test";
	psql -c "CREATE DATABASE artifice_scraper";
	psql -c "CREATE DATABASE artifice_scraper_test";
	artifice.scraper db init
	artifice.scraper db migrate
	artifice.scraper db upgrade
