poetry-lock:
	@poetry lock --no-update

poetry-sync:
	@poetry install --sync

poetry-export-reqs:
	poetry export --without-hashes -f requirements.txt -o requirements.txt

sync: poetry-lock poetry-sync poetry-export-reqs

black:
	black .

isort:
	isort .

ruff:
	ruff check . --fix

lint: isort black ruff

pytest_api_tests:
	pytest tests/api_tests -vvvvv

run_api_tests:
	docker compose up --build --abort-on-container-exit --exit-code-from api_tests
	docker compose stop
	docker compose rm -f api_tests
