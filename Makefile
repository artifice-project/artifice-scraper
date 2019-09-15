# https://krzysztofzuraw.com/blog/2016/makefiles-in-python-projects.html
.PHONY: clean-pyc clean-build
HOST=127.0.0.1
TEST_PATH=./
PACKAGE=Artifice
DATABASE=artifice_scraper
TEST_DATABASE=artifice_scraper_test
ENTRYPOINT=artifice.scraper

clean-pyc:
	@echo "//	clean-pyc"
	@echo "//		Remove python artifacts"
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +

clean-build:
	@echo "//	clean-build"
	@echo "//		Remove build artifacts."
	rm -rf build/
	rm -rf dist/
	rm -rf */$(PACKAGE).egg-info

clean: clean-pyc clean-build

build: clean
	@echo "//	build"
	@echo "//		Build source distribution & wheel"
	python3 setup.py sdist bdist_wheel

install: clean
	@echo "//	install"
	@echo "//		Install source editably"
	virtualenv env
	source env/bin/activate
	pip install -e .

reset-db:
	@echo "//	reset-db"
	@echo "//		Drop current database(s) and reset migrations"
	rm -rf migrations/
	psql -c "DROP DATABASE $(DATABASE)";
	psql -c "DROP DATABASE $(TEST_DATABASE)";

init-db:
	@echo "//	init-db"
	@echo "//		Create required databases and run migrations"
	psql -c "CREATE DATABASE $(DATABASE)";
	psql -c "CREATE DATABASE $(TEST_DATABASE)";
	$(ENTRYPOINT) db init
	$(ENTRYPOINT) db migrate
	$(ENTRYPOINT) db upgrade

database: reset-db init-db
