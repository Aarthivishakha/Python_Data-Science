"""CSV input and JSON output helpers."""
from __future__ import with_statement

import csv
import io
import json
import sys


def load_observations(path):
    """Load numeric feature/target pairs from a CSV file."""
    rows = []
    if sys.version_info[0] < 3:
        stream = open(path, "rb")
    else:
        stream = io.open(path, "r", newline="", encoding="utf-8")
    with stream:
        reader = csv.DictReader(stream)
        for line_number, row in enumerate(reader, 2):
            try:
                rows.append((float(row["feature"]), float(row["target"])))
            except (KeyError, TypeError, ValueError):
                raise ValueError("invalid observation on line %d" % line_number)
    if not rows:
        raise ValueError("dataset must contain at least one observation")
    return rows


def write_report(path, report):
    """Persist a deterministic JSON analysis report."""
    with open(path, "w") as stream:
        json.dump(report, stream, indent=2, sort_keys=True)
        stream.write("\n")
