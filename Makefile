# https://krzysztofzuraw.com/blog/2016/makefiles-in-python-projects.html
.PHONY: clean-pyc clean-build
HOST=127.0.0.1
TEST_PATH=./

clean-pyc:
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +

clean-build:
	rm -rf build/
	rm -rf dist/
	rm -rf *.egg-info



# @echo "    clean-pyc"
# @echo "        Remove python artifacts."
# @echo "    clean-build"
# @echo "        Remove build artifacts."
# @echo "    isort"
# @echo " 			 Sort import statements."
# @echo "    lint"
# @echo "        Check style with flake8."
# @echo "    test"
# @echo "        Run py.test"
# @echo '    run'
# @echo '        Run the `my_project` service on your local machine.'
# @echo '    docker-run'
# @echo '        Build and run the `my_project` service in a Docker container.'
