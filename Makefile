PYTHON ?= python3

.PHONY: install lint test check run

install:
	$(PYTHON) -m pip install -r requirements.txt

lint:
	$(PYTHON) -m ruff check .

test:
	$(PYTHON) -m pytest -q

check: lint test

run:
	$(PYTHON) -m src.main