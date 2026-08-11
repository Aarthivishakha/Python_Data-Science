from __future__ import with_statement

import os
import io
import tempfile
import unittest

from datascience.model import fit_linear_regression, predict
from datascience.pipeline import analyze, run


class PipelineTest(unittest.TestCase):
    def test_model_fits_linear_data(self):
        model = fit_linear_regression([(1.0, 3.0), (2.0, 5.0), (3.0, 7.0)])
        self.assertEqual(2.0, model["slope"])
        self.assertEqual(1.0, model["intercept"])
        self.assertEqual(9.0, predict(model, 4.0))

    def test_analysis_reports_zero_error(self):
        report = analyze([(1.0, 3.0), (2.0, 5.0), (3.0, 7.0)])
        self.assertEqual(3, report["feature_summary"]["count"])
        self.assertEqual(0.0, report["mean_absolute_error"])

    def test_pipeline_reads_and_writes_files(self):
        input_handle, input_path = tempfile.mkstemp(suffix=".csv")
        output_handle, output_path = tempfile.mkstemp(suffix=".json")
        os.close(input_handle)
        os.close(output_handle)
        try:
            with io.open(input_path, "w", encoding="utf-8") as stream:
                stream.write("feature,target\n1,3\n2,5\n")
            report = run(input_path, output_path)
            self.assertEqual(2, report["feature_summary"]["count"])
            self.assertTrue(os.path.getsize(output_path) > 0)
        finally:
            os.remove(input_path)
            os.remove(output_path)


if __name__ == "__main__":
    unittest.main()
