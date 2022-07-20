all: run

run:

	poetry run uvicorn API.kumiko_api:app --reload   
