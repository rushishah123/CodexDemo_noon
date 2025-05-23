# Codex Demo Noon

This repository demonstrates a simple Streamlit application for analyzing sales data from a CSV file. The app computes total revenue per product, shows a sales trend line chart over time and a bar chart of the top five best-selling products.

## Getting Started

1. Install Python dependencies (Streamlit and pandas). If running in a Codex environment, dependencies may already be installed, or you may need to add them to your setup.
    ```bash
    pip install streamlit pandas
    ```
2. Run the app:
    ```bash
    streamlit run sales_app.py
    ```
3. Upload a CSV file when prompted. A sample dataset is provided in `sample_sales.csv`.

## Sample Data

`sample_sales.csv` contains 50 rows of random sales data with the columns `Date`, `Product`, `Units` and `Price`.
