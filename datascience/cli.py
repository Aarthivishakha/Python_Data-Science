"""Command-line interface."""
from __future__ import print_function

from optparse import OptionParser

from datascience.pipeline import run


def main(argv=None):
    parser = OptionParser()
    parser.add_option("--input", dest="input_path")
    parser.add_option("--output", dest="output_path")
    options, _args = parser.parse_args(argv)
    if not options.input_path or not options.output_path:
        parser.error("--input and --output are required")
    report = run(options.input_path, options.output_path)
    print("analyzed %d observations" % report["feature_summary"]["count"])
    return 0


if __name__ == "__main__":
    main()
