# Data Science / ML Project (Python 3.16 development)

A reproducible machine-learning project that loads and validates CSV
observations, computes descriptive statistics, trains a univariate
least-squares regression model, evaluates prediction error, and writes a JSON
report. The implementation targets Python 3.16 and uses only the standard
library at runtime.

```bash
python setup.py test
python -m datascience.cli --input data/sample.csv --output reports/report.json
```

For a containerized run: `docker build -t data-science . && docker run --rm data-science`.

Python 3.16 is in early development, with alpha 1 scheduled for October 2026.
CI uses the supported `3.16-dev` selector. No official 3.16 container exists,
so the multi-stage Dockerfile builds the current CPython development source.
Ruff checks against its newest available `py315` grammar.

The sample dataset, ML pipeline, CLI, tests, and all 14 tool-trigger manifests are
connected to real repository files. Current analyzers run separately on Python
3.10+; the application itself remains Python 3.16 compatible.
