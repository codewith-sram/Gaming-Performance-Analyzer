
import os
import ast

print("=" * 45)
print(" GAMING PERFORMANCE ANALYZER")
print(" DAY 43 - PROJECT TESTING")
print("=" * 45)

# Check Python files
python_files = [
    file for file in os.listdir(".")
    if file.endswith(".py")
]

print("\n1. Python Files:")

for file in python_files:
    try:
        with open(file, "r", encoding="utf-8") as f:
            ast.parse(f.read())
        print(f"[PASS] {file}")
    except Exception as e:
        print(f"[ERROR] {file}: {e}")

# Check required files
print("\n2. Required Files:")

required_files = [
    "main.py",
    "README.md",
    "requirements.txt",
    "gaming_stats.csv"
]

for file in required_files:
    if os.path.exists(file):
        print(f"[PASS] {file} exists")
    else:
        print(f"[MISSING] {file}")

# Check dependencies
print("\n3. Required Libraries:")

libraries = ["pandas", "matplotlib", "numpy"]

for library in libraries:
    try:
        __import__(library)
        print(f"[PASS] {library} installed")
    except ImportError:
        print(f"[MISSING] {library} not installed")

print("\nDay 43 Testing Completed!")
print("=" * 45)
