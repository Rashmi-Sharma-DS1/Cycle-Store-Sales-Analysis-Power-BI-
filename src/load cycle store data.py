"""
Cycle Store Sales Analysis
Data Source Loader Script

Dataset:
https://www.kaggle.com/datasets/dillonmyrick/bike-store-sample-database

This script loads all 9 relational tables
from the Cycle Store dataset using kagglehub.
"""

import kagglehub
from kagglehub import KaggleDatasetAdapter


DATASET_NAME = "dillonmyrick/bike-store-sample-database"

TABLES = [
    "brands.csv",
    "categories.csv",
    "customers.csv",
    "orders.csv",
    "order_items.csv",
    "products.csv",
    "staffs.csv",
    "stores.csv",
    "stocks.csv"
]


def load_cycle_store_data():
    """
    Loads all Cycle Store CSV files into a dictionary of Pandas DataFrames.
    Returns:
        dict: {table_name: dataframe}
    """
    data = {}

    for table in TABLES:
        print(f"Loading {table}...")
        df = kagglehub.load_dataset(
            KaggleDatasetAdapter.PANDAS,
            DATASET_NAME,
            table
        )
        data[table.replace(".csv", "")] = df

    print("All tables loaded successfully ✅")
    return data


if __name__ == "__main__":
    cycle_data = load_cycle_store_data()

    # Example usage
    print("\nCustomers Table Preview:")
    print(cycle_data["customers"].head())
