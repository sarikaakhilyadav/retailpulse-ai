import sys
import unittest
from pathlib import Path

import pandas as pd

sys.path.insert(
    0,
    str(Path(__file__).resolve().parents[1] / "src")
)

from data_quality import (
    count_missing_values,
    count_duplicate_rows,
    count_non_positive_values,
    count_cancellations,
)


class TestDataQuality(unittest.TestCase):

    def setUp(self):
        self.df = pd.DataFrame({
            "Invoice": ["1001", "1001", "C1002", None],
            "Quantity": [2, 2, -1, 0],
            "Price": [10.0, 10.0, 5.0, None],
        })

    def test_missing_values(self):
        result = count_missing_values(self.df)
        self.assertEqual(result["Invoice"], 1)
        self.assertEqual(result["Price"], 1)

    def test_duplicate_rows(self):
        self.assertEqual(
            count_duplicate_rows(self.df), 1
        )

    def test_non_positive_quantities(self):
        self.assertEqual(
            count_non_positive_values(
                self.df, "Quantity"
            ), 2
        )

    def test_cancellations(self):
        self.assertEqual(
            count_cancellations(
                self.df, "Invoice"
            ), 1
        )

    def test_missing_column(self):
        with self.assertRaises(ValueError):
            count_non_positive_values(
                self.df, "Unknown"
            )


if __name__ == "__main__":
    unittest.main()
