# Data Science / ML Project (Python 2.6)

A reproducible machine-learning project that loads and validates CSV
observations, computes descriptive statistics, trains a univariate
least-squares regression model, evaluates prediction error, and writes a JSON
report. The implementation is compatible with Python 2.6 and uses only the
standard library at runtime.

```bash
python setup.py test
python -m datascience.cli --input data/sample.csv --output reports/report.json
```

The sample dataset, ML pipeline, CLI, tests, and all 14 tool-trigger manifests are
connected to real repository files. Current analyzers run separately on Python
3.10+; the application itself remains Python 2.6 compatible.
