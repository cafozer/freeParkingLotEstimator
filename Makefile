.PHONY:	fmt check test clean

 init:
	poetry install

 fmt:
	poetry run zimports -m parkingLotEstimator,tests src tests
	poetry run black src tests

 check:
	poetry run flake8
	poetry export -f requirements.txt | poetry run safety check --stdin
	poetry run mypy --allow-subclassing-any --ignore-missing-imports --strict --pretty src tests

 test:
	poetry run pytest

 clean:
	find . -name "*pyc" -o -name "*pyo" | xargs rm
	find . -name "__pycache__" | xargs rmdir