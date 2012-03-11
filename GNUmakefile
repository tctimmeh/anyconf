PYTHON ?= `which python`
VIRTUAL_ENV_NAME ?= venv

TEST_CMD = python --version && py.test test -q

.PHONY: all test upload setup

all: test
	./setup.py sdist bdist_egg

test:
	$(TEST_CMD)

testall:
	for venv in $(VIRTUAL_ENV_NAME)*; do if [ -d $$venv ]; then . $$venv/bin/activate && $(TEST_CMD); fi; done

upload: test
	./setup.py sdist bdist_egg upload

setup:
	./create-dev-env.py --env $(VIRTUAL_ENV_NAME) --python $(PYTHON)

