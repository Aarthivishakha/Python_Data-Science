.PHONY: test run analyze

test:
	python setup.py test

run:
	python -m datascience.cli --input data/sample.csv --output reports/report.json

analyze:
	python tool-triggers/beniget/run_beniget.py datascience
	python tool-triggers/pydriller/run_pydriller.py .
