dev-up:
	docker-compose up --build

test:
	pytest --cov=app tests/

format:
	black .
	isort .

type-check:
	mypy app/
