# Integrated tool triggers (Python 3.4 source)

All 14 manifests analyze the real `datascience/` package, `tests/`, dependency
files, dataset, or Git history. The application source is intentionally valid
under both Python 3.4 and the isolated Python 3.10+ analyzer environment.

| # | Trigger | Tool(s) | Integrated project input | Purpose |
|---:|---|---|---|---|
| 1 | `beniget` | Beniget | `datascience/**/*.py` | Def-use/data-flow analysis |
| 2 | `cognitive-ast` | complexipy | `datascience/**/*.py` | Cognitive complexity |
| 3 | `cosmic-ray` | Cosmic Ray | model + pipeline tests | Mutation testing |
| 4 | `coverage-py` | coverage.py | package + tests | Statement/branch coverage |
| 5 | `coverage-py-beniget` | coverage.py + Beniget | package + tests | Coverage plus data flow |
| 6 | `crosshair` | CrossHair | statistics + model | Symbolic path/contract analysis |
| 7 | `jscpd` | jscpd | package + tests | Duplicate-code detection |
| 8 | `pip-audit` | pip-audit | runtime + analyzer requirements | Dependency vulnerabilities |
| 9 | `pydriller` | PyDriller | `datascience/` Git history | Code churn/history analysis |
| 10 | `pylint` | Pylint | package + tests | Static lint analysis |
| 11 | `pymcdc` | pymcdc | pipeline + tests | Condition/decision coverage |
| 12 | `radon-lizard` | Radon + Lizard | `datascience/**/*.py` | Cyclomatic complexity |
| 13 | `semgrep-bandit` | Semgrep + Bandit | `datascience/**/*.py` | Security SAST |
| 14 | `testmon` | pytest-testmon | package + tests | Change-aware test selection |

Each directory contains a `trigger.yaml` declaring the Python 3.4 source
version, isolated analyzer runtime, exact target files, and executable command.
`cosmic-ray/cosmic-ray.toml` mutates the real regression model and executes the
real pipeline tests. The helper scripts run Beniget over source ASTs and
PyDriller over repository history; there are no disconnected sample fixtures.

Install analyzer dependencies only in Python 3.10+:

```bash
python -m pip install -r tool-triggers/requirements.txt
```
