create-requirements-file:
	pip freeze > requirements.txt

run-local:
	poetry run super_tester

build-image:
	docker build -t super-testing .
	