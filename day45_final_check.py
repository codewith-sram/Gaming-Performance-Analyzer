
# Gaming Performance Analyzer
# Day 45 - Final Project Verification

import os
import ast
import pandas as pd

print("=" * 55)
print("       GAMING PERFORMANCE ANALYZER")
print("          FINAL PROJECT AUDIT")
print("=" * 55)

# 1. Check project files
print("\n1. PROJECT FILE VERIFICATION")

required_files = [
    "main.py",
    "README.md",
    "requirements.txt",
    "gaming_stats.csv",
    "gaming_model.pkl",
    "day44_report.py",
    "gaming_performance_report.csv"
]

for file in required_files:
    if os.path.exists(file):
        print(f"[PASS] {file}")
    else:
        print(f"[MISSING] {file}")

# 2. Check Python syntax
print("\n2. PYTHON CODE VERIFICATION")

python_files = [
    file for file in os.listdir(".")
    if file.endswith(".py")
]

for file in python_files:
    try:
        with open(file, "r", encoding="utf-8") as f:
            ast.parse(f.read())

        print(f"[PASS] {file} syntax is correct")

    except Exception as e:
        print(f"[ERROR] {file}: {e}")

# 3. Check dataset
print("\n3. DATASET VERIFICATION")

try:
    data = pd.read_csv("gaming_stats.csv")

    print("[PASS] Dataset loaded successfully")
    print("Total Rows:", len(data))
    print("Total Columns:", len(data.columns))

except Exception as e:
    print("[ERROR] Dataset:", e)

# 4. Check performance report
print("\n4. PERFORMANCE REPORT")

try:
    report = pd.read_csv("gaming_performance_report.csv")

    print("[PASS] Performance report found")
    print("Report Rows:", len(report))

except Exception as e:
    print("[ERROR] Report:", e)

# 5. Final message
print("\n" + "=" * 55)
print("       FINAL PROJECT CHECK COMPLETED")
print("=" * 55)

print("\nCongratulations!")
print("Your 45-Day Project Journey is Complete!")

