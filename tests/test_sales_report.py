import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

import pandas as pd

sys.path.insert(
    0,
    str(Path(__file__).resolve().parents[1] / "src")
)

import generate_sales_report


class TestSalesReport(unittest.TestCase):

    def test_csv_report_export(self):
        sample = pd.DataFrame({
            "Invoice": ["1001", "1002"],
            "Quantity": [2, 3],
            "Price": [10.0, 5.0],
        })

        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            workbook_path = root / "sample.xlsx"
            output_path = root / "sales_kpi_summary.csv"

            sample.to_excel(workbook_path, index=False)

            with patch.object(
                generate_sales_report,
                "DATASET_PATH",
                workbook_path,
            ), patch.object(
                generate_sales_report,
                "OUTPUT_PATH",
                output_path,
            ):
                generate_sales_report.generate_sales_report()

            self.assertTrue(output_path.exists())

            report = pd.read_csv(output_path)

            self.assertEqual(len(report), 1)
            self.assertEqual(
                report.loc[0, "total_revenue"], 35.0
            )
            self.assertEqual(
                report.loc[0, "total_units_sold"], 5
            )
            self.assertEqual(
                report.loc[0, "total_transactions"], 2
            )
            self.assertEqual(
                report.loc[0, "average_order_value"], 17.5
            )


if __name__ == "__main__":
    unittest.main()
