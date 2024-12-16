start:
	uvicorn src.main:app --reload

up:
	docker compose up

my_test:
	pytest .

cov:
	pytest --cov=.