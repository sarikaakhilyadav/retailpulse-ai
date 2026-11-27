
# RetailPulse AI — Local Setup Guide

## 1. Prerequisites

- Python 3.11
- Git
- Visual Studio Code

## 2. Clone the Repository

    git clone https://github.com/sarikaakhilyadav/retailpulse-ai.git
    cd retailpulse-ai

## 3. Install Dependencies

    python -m pip install -r requirements.txt

## 4. Run Automated Tests

    python -m unittest discover -s tests -v

Check that all tests pass before continuing.

## 5. Generate Sample Data

    python src/generate_sample_data.py

## 6. Generate Sales Reports

    python src/generate_sales_report.py --dataset data/sample_retail.xlsx

## 7. Expected Output Files

- reports/sales_kpi_summary.csv
- reports/monthly_sales.csv

## 8. Use the Real Retail Dataset

Download the Online Retail II dataset from:

https://archive.ics.uci.edu/dataset/502/online+retail+ii

Extract the Excel workbook into the data directory
and name it online_retail_II.xlsx.

Run:

    python src/generate_sales_report.py

## 9. Troubleshooting

- Verify that all dependencies are installed.
- Check the dataset filename and location.
- Ensure required dataset columns are available.
- Review automated test logs for failures.

## 10. Validation Status

Local execution with the complete retail dataset
is pending verification.
