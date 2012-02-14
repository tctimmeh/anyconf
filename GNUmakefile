PYTHON ?= `which python`
VIRTUAL_ENV ?= venv

all:
	echo "Nothing to do"

upload:
	./setup.py sdist bdist_egg upload

setup:
	$(PYTHON) create-dev-env.py --env $(VIRTUAL_ENV)

