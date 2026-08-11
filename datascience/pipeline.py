"""End-to-end analysis orchestration."""

from datascience.io import load_observations, write_report
from datascience.model import fit_linear_regression, predict
from datascience.statistics import summarize


def analyze(observations):
    observations = list(observations)
    model = fit_linear_regression(observations)
    errors = [row[1] - predict(model, row[0]) for row in observations]
    return {
        "feature_summary": summarize(row[0] for row in observations),
        "target_summary": summarize(row[1] for row in observations),
        "model": model,
        "mean_absolute_error": sum(abs(error) for error in errors) / float(len(errors)),
    }


def run(input_path, output_path):
    report = analyze(load_observations(input_path))
    write_report(output_path, report)
    return report
