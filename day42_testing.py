
import os
import importlib.util
import pandas as pd
import joblib

DATA_FILE = "gaming_stats.csv"
MODEL_FILE = "gaming_model.pkl"
APP_FILE = "day41_app.py"
REPORT_FILE = "day42_test_report.csv"

test_results = []


def record_test(test_name, status, details):
    test_results.append({
        "Test": test_name,
        "Status": status,
        "Details": details
    })

    symbol = "PASS" if status == "PASS" else "FAIL"

    print(f"[{symbol}] {test_name}")
    print(f"       {details}")


def test_project_files():
    print("\n1. PROJECT FILE TESTING")
    print("-" * 45)

    required_files = [
        APP_FILE,
        DATA_FILE,
        MODEL_FILE
    ]

    for file_name in required_files:
        if os.path.exists(file_name):
            record_test(
                f"Check {file_name}",
                "PASS",
                "File exists in project folder."
            )
        else:
            record_test(
                f"Check {file_name}",
                "FAIL",
                "File is missing."
            )


def test_dependencies():
    print("\n2. LIBRARY TESTING")
    print("-" * 45)

    libraries = [
        "pandas",
        "matplotlib",
        "sklearn",
        "joblib",
        "tkinter"
    ]

    for library in libraries:
        try:
            if importlib.util.find_spec(library) is not None:
                record_test(
                    f"Check {library}",
                    "PASS",
                    "Library is available."
                )
            else:
                record_test(
                    f"Check {library}",
                    "FAIL",
                    "Library is not available."
                )
        except (ImportError, ValueError):
            record_test(
                f"Check {library}",
                "FAIL",
                "Could not check library."
            )


def test_dataset():
    print("\n3. DATASET TESTING")
    print("-" * 45)

    if not os.path.exists(DATA_FILE):
        record_test(
            "Load gaming dataset",
            "FAIL",
            "gaming_stats.csv is missing."
        )
        return None

    try:
        data = pd.read_csv(DATA_FILE)

        record_test(
            "Load gaming dataset",
            "PASS",
            f"Loaded {len(data)} rows."
        )

        required_columns = ["Kills", "Deaths", "Assists"]

        missing_columns = [
            column for column in required_columns
            if column not in data.columns
        ]

        if missing_columns:
            record_test(
                "Check dataset columns",
                "FAIL",
                f"Missing columns: {missing_columns}"
            )
            return None

        record_test(
            "Check dataset columns",
            "PASS",
            "Kills, Deaths and Assists are present."
        )

        clean_data = data.copy()

        for column in required_columns:
            clean_data[column] = pd.to_numeric(
                clean_data[column], errors="coerce"
            )

        invalid_rows = clean_data[required_columns].isna().any(axis=1).sum()

        if invalid_rows == 0:
            record_test(
                "Check numeric data",
                "PASS",
                "All required values are numeric."
            )
        else:
            record_test(
                "Check numeric data",
                "FAIL",
                f"{invalid_rows} rows contain missing or invalid values."
            )

        valid_data = clean_data.dropna(
            subset=required_columns
        )

        if len(valid_data) > 0:
            record_test(
                "Check valid match records",
                "PASS",
                f"{len(valid_data)} valid matches found."
            )
            return valid_data
        else:
            record_test(
                "Check valid match records",
                "FAIL",
                "No valid match records found."
            )
            return None

    except Exception as error:
        record_test(
            "Read gaming dataset",
            "FAIL",
            str(error)
        )
        return None


def test_model(data):
    print("\n4. MACHINE LEARNING MODEL TESTING")
    print("-" * 45)

    if not os.path.exists(MODEL_FILE):
        record_test(
            "Load saved model",
            "FAIL",
            "gaming_model.pkl is missing."
        )
        return

    try:
        model = joblib.load(MODEL_FILE)

        record_test(
            "Load saved model",
            "PASS",
            "Saved model loaded successfully."
        )

    except Exception as error:
        record_test(
            "Load saved model",
            "FAIL",
            str(error)
        )
        return

    if data is None:
        record_test(
            "Test model prediction",
            "FAIL",
            "Valid dataset is unavailable."
        )
        return

    try:
        features = data[["Deaths", "Assists"]].head(5)

        predictions = model.predict(features)

        if len(predictions) == len(features):
            record_test(
                "Test model prediction",
                "PASS",
                f"Successfully predicted {len(predictions)} matches."
            )
        else:
            record_test(
                "Test model prediction",
                "FAIL",
                "Prediction count does not match input count."
            )

    except Exception as error:
        record_test(
            "Test model prediction",
            "FAIL",
            str(error)
        )


def save_test_report():
    print("\n5. SAVING TEST REPORT")
    print("-" * 45)

    report = pd.DataFrame(test_results)

    try:
        report.to_csv(REPORT_FILE, index=False)

        print(f"Test report saved: {REPORT_FILE}")

    except Exception as error:
        print("Could not save report:", error)


def show_summary():
    print("\n" + "=" * 45)
    print("         FINAL TEST SUMMARY")
    print("=" * 45)

    total = len(test_results)

    passed = sum(
        result["Status"] == "PASS"
        for result in test_results
    )

    failed = total - passed

    print(f"Total Tests: {total}")
    print(f"Passed: {passed}")
    print(f"Failed: {failed}")

    if failed == 0:
        print("\nAll tests passed successfully!")
    else:
        print("\nSome tests failed. Check the report.")

    print("=" * 45)


def main():
    print("=" * 45)
    print(" GAMING PERFORMANCE ANALYZER - DAY 42")
    print(" Project Testing and Bug Detection")
    print("=" * 45)

    test_project_files()
    test_dependencies()

    data = test_dataset()
    test_model(data)

    save_test_report()
    show_summary()

    print("\nDay 42 testing completed!")


if __name__ == "__main__":
    main()
