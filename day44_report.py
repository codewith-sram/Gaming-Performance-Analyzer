
# Gaming Performance Analyzer
# Day 44 - Automatic Performance Report

import pandas as pd
import os

print("=" * 45)
print(" GAMING PERFORMANCE REPORT GENERATOR")
print("=" * 45)

# Load gaming dataset
file_path = "gaming_stats.csv"

if os.path.exists(file_path):

    data = pd.read_csv(file_path)

    print("\nDataset loaded successfully!")

    # Select numeric columns
    numeric_data = data.select_dtypes(include="number")

    if not numeric_data.empty:

        # Generate performance summary
        report = numeric_data.describe().T

        # Add average values
        report["Average"] = numeric_data.mean()

        # Save report
        report.to_csv("gaming_performance_report.csv")

        print("\nPerformance Report Generated!")

        print("\nReport Preview:")
        print(report)

        print("\nReport saved as:")
        print("gaming_performance_report.csv")

    else:
        print("No numeric columns found in dataset.")

else:
    print("Error: gaming_stats.csv not found!")

print("\nDay 44 Completed!")
print("=" * 45)
