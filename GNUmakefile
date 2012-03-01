PYTHON ?= `which python`
VIRTUAL_ENV ?= venv

TEST_CMD = py.test test

.PHONY: all test upload setup

all: test
	./setup.py sdist bdist_egg

test:
	$(TEST_CMD)

testall:
	@for venv in $(VIRTUAL_ENV)*; do if [ -d $$venv ]; then . $$venv/bin/activate && $(TEST_CMD); fi; done

upload: test
	./setup.py sdist bdist_egg upload

setup:
	./create-dev-env.py --env $(VIRTUAL_ENV) --python $(PYTHON)

