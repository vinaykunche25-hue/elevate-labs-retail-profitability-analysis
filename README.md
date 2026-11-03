# Retail Business Performance & Profitability Analysis

## Overview
End-to-end retail analytics portfolio project covering sales, profit, category/sub-category performance, regional contribution, discounts and inventory holding days.

**Dataset disclosure:** The dataset was generated synthetically with a fixed random seed for learning. It is not real company data. Currency values are illustrative USD.

## Project files
- `data/raw/retail_transactions_raw.csv` — raw data with intentionally introduced missing values and duplicate rows.
- `data/cleaned/retail_transactions_cleaned.csv` — cleaned analysis dataset.
- `data/cleaned/` — category, region and sub-category summary CSVs.
- `sql/retail_analysis.sql` — MySQL KPI, profitability, regional, discount, inventory and monthly queries; view and indexes.
- `python/retail_analysis.ipynb` — Jupyter analysis notebook.
- `python/retail_analysis.py` — code-only notebook version.
- `dashboard/interactive_dashboard.html` — interactive browser dashboard with region/category/channel filters.
- `reports/final_project_report.pdf` — concise report.
- `visualizations/` — exported charts.

## Run the project
1. Install dependencies: `pip install -r requirements.txt`
2. Open `python/retail_analysis.ipynb` in Jupyter or VS Code and run cells in order.
3. Open `dashboard/interactive_dashboard.html` in a browser.
4. Import `data/cleaned/retail_transactions_cleaned.csv` into MySQL as `retail_transactions` and run `sql/retail_analysis.sql`.

## Sample dataset KPIs
- Sales: 1,519,413.46
- Profit: 702,972.17
- Profit margin: 46.27%
- Distinct orders: 917
- Distinct customers: 554

These figures describe only the synthetic dataset. Do not present them as actual business performance.

## Limitations
This is a practice dataset. Correlation does not prove causation. The supplied dashboard is browser-based HTML, not a native Tableau workbook or Power BI `.pbix`; the cleaned CSV can be imported into either tool to build a native dashboard.
