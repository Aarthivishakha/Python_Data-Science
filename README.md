# Data Science Pipeline (Python 3.14)

A small, reproducible data-science project that loads CSV observations,
computes descriptive statistics, fits a univariate least-squares model, and
writes a JSON report. The implementation is compatible with Python 3.14 and
uses only the standard library at runtime.

```bash
python setup.py test
python -m datascience.cli --input data/sample.csv --output reports/report.json
```

For a containerized run: `docker build -t data-science . && docker run --rm data-science`.

The sample dataset, pipeline, CLI, tests, and all 14 tool-trigger manifests are
connected to real repository files. Current analyzers run separately on Python
3.10+; the application itself remains Python 3.14 compatible.
