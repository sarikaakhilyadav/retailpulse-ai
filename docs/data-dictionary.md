# RetailPulse AI — Data Dictionary

## Dataset Overview

RetailPulse AI uses the UCI Online Retail II dataset to analyse retail transactions, customer purchasing behaviour, and sales trends.

## Dataset Columns

| Column | Description |
|---|---|
| Invoice | Invoice number; values beginning with C indicate cancellations. |
| StockCode | Product code. |
| Description | Product name or description. |
| Quantity | Number of units purchased or returned. |
| InvoiceDate | Date and time of the transaction. |
| Price | Unit price in GBP. |
| Customer ID | Customer identifier. |
| Country | Country associated with the transaction. |

## Calculated Metrics

| Metric | Calculation |
|---|---|
| Revenue | Quantity × Price |
| Total Revenue | Sum of valid sales revenue |
| Units Sold | Sum of valid sales quantities |
| Total Transactions | Number of unique valid invoices |
| Average Order Value | Total Revenue ÷ Total Transactions |
| Monthly Revenue | Revenue grouped by month |

## Data Quality Rules

- Exclude cancelled invoices from sales calculations.
- Exclude zero or negative quantities.
- Exclude zero or negative prices.
- Check missing values and duplicate records.
- Validate dates before monthly aggregation.

## Purpose

This document defines the dataset fields and metrics used in RetailPulse AI, keeping Python analysis, SQL queries, and future Power BI dashboards consistent.
