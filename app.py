
import os
import joblib
import pandas as pd

DATA_FILE = "gaming_stats.csv"
MODEL_FILE = "gaming_model.pkl"


def load_data():
    """Load and validate the gaming dataset."""
    if not os.path.exists(DATA_FILE):
        print(f"\nError: {DATA_FILE} was not found.")
        return None

    try:
        data = pd.read_csv(DATA_FILE)
        required = ["Kills", "Deaths", "Assists"]

        if not all(column in data.columns for column in required):
            print("\nThe dataset must contain Kills, Deaths and Assists.")
            print("Available columns:", list(data.columns))
            return None

        for column in required:
            data[column] = pd.to_numeric(
                data[column], errors="coerce"
            )

        data = data.dropna(subset=required)

        if data.empty:
            print("\nNo valid match records were found.")
            return None

        return data

    except Exception as error:
        print("Could not read the dataset:", error)
        return None


def show_statistics():
    """Display basic gaming statistics."""
    data = load_data()

    if data is None:
        return

    print("\n========== GAMING STATISTICS ==========")
    print(f"Total matches: {len(data)}")
    print(f"Total kills: {data['Kills'].sum():.0f}")
    print(f"Total deaths: {data['Deaths'].sum():.0f}")
    print(f"Total assists: {data['Assists'].sum():.0f}")
    print(f"Average kills: {data['Kills'].mean():.2f}")
    print(f"Average deaths: {data['Deaths'].mean():.2f}")
    print(f"Average assists: {data['Assists'].mean():.2f}")

    kd_ratio = (
        data["Kills"].sum() / data["Deaths"].sum()
        if data["Deaths"].sum() != 0
        else float("inf")
    )

    if kd_ratio == float("inf"):
        print("Overall K/D ratio: Undefined (zero total deaths)")
    else:
        print(f"Overall K/D ratio: {kd_ratio:.2f}")

    print("\nFirst five matches:")
    print(data.head().to_string(index=False))


def predict_kills():
    """Predict kills using the saved Day 33 model."""
    if not os.path.exists(MODEL_FILE):
        print(f"\nError: {MODEL_FILE} was not found.")
        print("Run your Day 33 program first.")
        return

    try:
        model = joblib.load(MODEL_FILE)

        deaths = int(input("Enter expected deaths: "))
        assists = int(input("Enter expected assists: "))

        if deaths < 0 or assists < 0:
            print("Values cannot be negative.")
            return

        input_data = pd.DataFrame(
            [{"Deaths": deaths, "Assists": assists}]
        )

        prediction = model.predict(input_data)[0]

        print("\n========== PREDICTION ==========")
        print(f"Deaths entered: {deaths}")
        print(f"Assists entered: {assists}")
        print(f"Estimated kills: {prediction:.2f}")

        save = input("\nSave this prediction to CSV? (y/n): ").strip().lower()

        if save == "y":
            result = pd.DataFrame([{
                "Deaths": deaths,
                "Assists": assists,
                "Predicted_Kills": round(float(prediction), 2)
            }])

            file_name = "day37_predictions.csv"

            if os.path.exists(file_name):
                result.to_csv(
                    file_name, mode="a", header=False, index=False
                )
            else:
                result.to_csv(file_name, index=False)

            print(f"Prediction saved to {file_name}")

    except ValueError:
        print("Please enter valid whole numbers.")
    except Exception as error:
        print("Prediction failed:", error)


def export_report():
    """Export a cleaned copy of the gaming dataset."""
    data = load_data()

    if data is None:
        return

    file_name = "day37_gaming_report.csv"

    try:
        data.to_csv(file_name, index=False)
        print(f"\nReport exported successfully: {file_name}")
    except Exception as error:
        print("Could not export report:", error)


def show_menu():
    """Display the application menu."""
    print("\n" + "=" * 45)
    print("      GAMING PERFORMANCE ANALYZER")
    print("=" * 45)
    print("1. View Gaming Statistics")
    print("2. Predict Kills")
    print("3. Export Gaming Report")
    print("4. View Dataset Information")
    print("5. Exit")
    print("=" * 45)


def show_dataset_info():
    """Display dataset structure and summary."""
    data = load_data()

    if data is None:
        return

    print("\n========== DATASET INFORMATION ==========")
    print(f"Rows: {data.shape[0]}")
    print(f"Columns: {data.shape[1]}")
    print("\nColumn names:")
    print(", ".join(data.columns))
    print("\nStatistical summary:")
    print(data.describe().round(2).to_string())


def main():
    print("\nWelcome to Gaming Performance Analyzer!")

    while True:
        show_menu()
        choice = input("Enter your choice (1-5): ").strip()

        if choice == "1":
            show_statistics()
        elif choice == "2":
            predict_kills()
        elif choice == "3":
            export_report()
        elif choice == "4":
            show_dataset_info()
        elif choice == "5":
            print("\nThank you for using Gaming Performance Analyzer!")
            break
        else:
            print("\nInvalid choice. Please enter a number from 1 to 5.")


if __name__ == "__main__":
    main()
