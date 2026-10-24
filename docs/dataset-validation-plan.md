# Dataset Validation Plan

## Objective

Define the checks required before using the Online Retail II dataset for RetailPulse AI.

## 1. Data Structure

- [ ] Verify worksheet names and row counts
- [ ] Identify column names and data types
- [ ] Check missing values
- [ ] Investigate duplicate records

## 2. Transaction Quality

- [ ] Identify cancelled orders and returns
- [ ] Check negative or zero quantities
- [ ] Investigate invalid prices
- [ ] Validate transaction dates

## 3. Dashboard Requirements

- [ ] Sales: Confirm revenue and date fields
- [ ] Products: Verify product identifiers
- [ ] Customers: Assess missing customer IDs
- [ ] Forecasting: Evaluate historical sales continuity

## 4. Acceptance Criteria

The dataset should support meaningful sales, product, customer and forecasting analysis. Any limitations must be documented before development.

## Next Steps

Download the original dataset, inspect it using Python and Pandas, and document the validation findings.

**Status:** Validation planned; not yet performed.
