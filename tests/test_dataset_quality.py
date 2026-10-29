import unittest
import pandas as pd


class TestDatasetQuality(unittest.TestCase):

    def setUp(self):
        self.data = pd.DataFrame({
            "Invoice": ["1001", "1002", "C1003", "1004"],
            "Quantity": [2, 3, -1, 0],
            "Price": [10.0, 15.0, 5.0, 0.0]
        })

    def test_missing_values(self):
        self.assertEqual(
            self.data.isnull().sum().sum(), 0
        )

    def test_non_positive_quantities(self):
        count = (self.data["Quantity"] <= 0).sum()
        self.assertEqual(count, 2)

    def test_non_positive_prices(self):
        count = (self.data["Price"] <= 0).sum()
        self.assertEqual(count, 1)

    def test_cancellations(self):
        count = (
            self.data["Invoice"]
            .astype(str)
            .str.startswith("C")
            .sum()
        )
        self.assertEqual(count, 1)


if __name__ == "__main__":
    unittest.main()
