
# Gaming Performance Analyzer
# Day 42 - Code Cleaning and Improvement

import pandas as pd
import matplotlib.pyplot as plt


# Load gaming dataset
def load_data(file_path):
    try:
        data = pd.read_csv(file_path)
        print("Dataset loaded successfully!")
        return data

    except FileNotFoundError:
        print("Error: Dataset file not found!")
        return None


# Display basic information
def show_data_info(data):
    if data is not None:
        print("\nDataset Information:")
        print(data.info())

        print("\nFirst Five Records:")
        print(data.head())


# Calculate average gaming performance
def calculate_average(data):
    if data is not None:
        numeric_data = data.select_dtypes(include="number")

        print("\nAverage Performance:")
        print(numeric_data.mean())


# Main function
def main():
    file_path = "gaming_stats.csv"

    data = load_data(file_path)

    if data is not None:
        show_data_info(data)
        calculate_average(data)

    print("\nGaming Performance Analyzer Completed!")


# Run the program
if __name__ == "__main__":
    main()
