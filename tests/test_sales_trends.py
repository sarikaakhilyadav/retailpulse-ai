import sys
import unittest
from pathlib import Path

import pandas as pd

sys.path.insert(
    0,
    str(Path(__file__).resolve().parents[1] / "src")
)

from sales_trends import calculate_monthly_sales


class TestMonthlySales(unittest.TestCase):

    def setUp(self):
        self.df = pd.DataFrame({
            "Invoice": [
                "1001", "1002", "1003", "C1004"
            ],
            "InvoiceDate": [
                "2026-01-05",
                "2026-01-15",
                "2026-02-10",
                "2026-02-12",
            ],
            "Quantity": [2, 3, 1, -1],
            "Price": [10.0, 5.0, 20.0, 10.0],
        })

    def test_monthly_revenue(self):
        result = calculate_monthly_sales(self.df)

        self.assertEqual(len(result), 2)
        self.assertEqual(
            result.loc[0, "Month"], "2026-01"
        )
        self.assertEqual(
            result.loc[0, "TotalRevenue"], 35.0
        )
        self.assertEqual(
            result.loc[1, "Month"], "2026-02"
        )
        self.assertEqual(
            result.loc[1, "TotalRevenue"], 20.0
        )

    def test_excludes_cancellations(self):
        result = calculate_monthly_sales(self.df)
        self.assertEqual(
            result["TotalRevenue"].sum(), 55.0
        )

    def test_missing_required_column(self):
        df = self.df.drop(
            columns=["InvoiceDate"]
        )

        with self.assertRaises(ValueError):
            calculate_monthly_sales(df)


if __name__ == "__main__":
    unittest.main()
