test:
	python -m pytest --durations=3 -vv

test-cov:
	python -m pytest --durations=3 -vv --cov-config=.coveragerc --cov-report html --cov