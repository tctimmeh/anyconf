PYTHON ?= `which python`
VIRTUAL_ENV ?= venv

.PHONY: all test upload setup

all: test
	./setup.py sdist bdist_egg

test:
	py.test test

upload: test
	./setup.py sdist bdist_egg upload

setup:
	./create-dev-env.py --env $(VIRTUAL_ENV) --python $(PYTHON)

