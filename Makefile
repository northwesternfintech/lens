.PHONY: install
install:
	poetry install

.PHONY: test
test:
	poetry run pytest .

.PHONY: lint
lint:
	poetry run mypy lens
	poetry run ruff check lens
	poetry run ruff format --check lens

.PHONY: format
format:
	poetry run ruff format lens
	poetry run ruff check --fix lens
