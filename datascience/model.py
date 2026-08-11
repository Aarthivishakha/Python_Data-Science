"""A minimal univariate least-squares regression model."""

from datascience.statistics import mean


def fit_linear_regression(observations):
    """Return slope and intercept for feature/target pairs."""
    observations = list(observations)
    if len(observations) < 2:
        raise ValueError("regression requires at least two observations")
    feature_mean = mean(row[0] for row in observations)
    target_mean = mean(row[1] for row in observations)
    denominator = sum((row[0] - feature_mean) ** 2 for row in observations)
    if denominator == 0:
        raise ValueError("features must not all be identical")
    numerator = sum(
        (row[0] - feature_mean) * (row[1] - target_mean)
        for row in observations
    )
    slope = numerator / denominator
    return {"slope": slope, "intercept": target_mean - slope * feature_mean}


def predict(model, feature):
    return model["slope"] * feature + model["intercept"]
