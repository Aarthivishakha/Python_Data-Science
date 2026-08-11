# Data Science / ML Project (Python 3.15 pre-release)

A reproducible machine-learning project that loads and validates CSV
observations, computes descriptive statistics, trains a univariate
least-squares regression model, evaluates prediction error, and writes a JSON
report. The implementation targets Python 3.15 and uses only the standard
library at runtime.

```bash
python setup.py test
python -m datascience.cli --input data/sample.csv --output reports/report.json
```

For a containerized run: `docker build -t data-science . && docker run --rm data-science`.

Python 3.15 remains pre-release. CI pins the current beta and Docker uses the
official rolling `3.15-rc-slim` image.

The sample dataset, ML pipeline, CLI, tests, and all 14 tool-trigger manifests are
connected to real repository files. Current analyzers run separately on Python
3.10+; the application itself remains Python 3.15 compatible.
