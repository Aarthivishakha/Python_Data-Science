"""Descriptive statistics without external dependencies."""


def mean(values):
    values = list(values)
    if not values:
        raise ValueError("mean requires at least one value")
    return sum(values) / float(len(values))


def summarize(values):
    values = list(values)
    if not values:
        raise ValueError("summary requires at least one value")
    average = mean(values)
    variance = sum((value - average) ** 2 for value in values) / float(len(values))
    return {
        "count": len(values),
        "mean": average,
        "minimum": min(values),
        "maximum": max(values),
        "variance": variance,
    }
