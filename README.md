# Data Science / ML Project (Python 3.4)

A reproducible machine-learning project that loads and validates CSV
observations, computes descriptive statistics, trains a univariate
least-squares regression model, evaluates prediction error, and writes a JSON
report. The implementation is compatible with Python 3.4 and uses only the
standard library at runtime.

```bash
python setup.py test
python -m datascience.cli --input data/sample.csv --output reports/report.json
```

The sample dataset, ML pipeline, CLI, tests, and all 14 tool-trigger manifests are
connected to real repository files. Current analyzers run separately on Python
3.10+; the application itself remains Python 3.4 compatible.

## Project flow

1. `datascience/io.py` validates and loads `data/sample.csv`.
2. `datascience/statistics.py` computes count, mean, range, and variance.
3. `datascience/model.py` trains a least-squares linear-regression model and predicts values.
4. `datascience/pipeline.py` evaluates mean absolute error and assembles the report.
5. `datascience/cli.py` connects the pipeline to command-line input and JSON output.
6. `tests/test_pipeline.py` checks training, prediction, evaluation, and file integration.

The input schema is `feature,target`, with numeric values and at least two rows
for model training. The generated JSON contains feature and target summaries,
the trained slope/intercept, and mean absolute error.

## Repository structure

- `data/`: version-controlled sample observations.
- `datascience/`: ingestion, statistics, model, pipeline, and CLI modules.
- `tests/`: unit and end-to-end pipeline tests.
- `tool-triggers/`: 14 analyzer manifests and their helper/configuration files.
- `setup.py`: Python 3.4-compatible packaging and console entry point.
- `Makefile`: test, pipeline, and analyzer shortcuts.

See `tool-triggers/README.md` for every tool command, purpose, and exact project input.
