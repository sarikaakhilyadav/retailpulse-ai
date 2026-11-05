import sys
import unittest
from pathlib import Path

import pandas as pd

sys.path.insert(
    0,
    str(Path(__file__).resolve().parents[1] / "src")
)

from sales_kpis import calculate_sales_kpis


class TestSalesKPIs(unittest.TestCase):

    def setUp(self):
        self.df = pd.DataFrame({
            "Invoice": ["1001", "1002", "1003"],
            "Quantity": [2, 3, 1],
            "Price": [10.0, 15.0, 20.0],
        })

    def test_total_revenue(self):
        result = calculate_sales_kpis(self.df)
        self.assertEqual(
            result["total_revenue"], 85.0
        )

    def test_total_units_sold(self):
        result = calculate_sales_kpis(self.df)
        self.assertEqual(
            result["total_units_sold"], 6
        )

    def test_total_transactions(self):
        result = calculate_sales_kpis(self.df)
        self.assertEqual(
            result["total_transactions"], 3
        )

    def test_average_order_value(self):
        result = calculate_sales_kpis(self.df)
        self.assertEqual(
            result["average_order_value"], 28.33
        )

    def test_excludes_cancellations(self):
        df = pd.DataFrame({
            "Invoice": ["1001", "C1002"],
            "Quantity": [2, -1],
            "Price": [10.0, 15.0],
        })

        result = calculate_sales_kpis(df)
        self.assertEqual(
            result["total_revenue"], 20.0
        )

    def test_empty_dataframe(self):
        df = pd.DataFrame(
            columns=["Invoice", "Quantity", "Price"]
        )

        result = calculate_sales_kpis(df)
        self.assertEqual(
            result["total_revenue"], 0.0
        )
        self.assertEqual(
            result["average_order_value"], 0.0
        )

    def test_missing_required_column(self):
        df = pd.DataFrame({
            "Invoice": ["1001"],
            "Quantity": [2],
        })

        with self.assertRaises(ValueError):
            calculate_sales_kpis(df)


if __name__ == "__main__":
    unittest.main()
