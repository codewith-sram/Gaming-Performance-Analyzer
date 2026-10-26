
import os
import joblib
import pandas as pd
import matplotlib.pyplot as plt

MODEL_FILE = "gaming_model.pkl"
DATA_FILE = "gaming_stats.csv"
REPORT_FILE = "day36_error_analysis.csv"
CHART_FILE = "day36_error_analysis.png"


def main():
    print("=" * 50)
    print(" GAMING PERFORMANCE ANALYZER - DAY 36")
    print(" Prediction Error Analysis")
    print("=" * 50)

    # Check files
    if not os.path.exists(MODEL_FILE):
        print(f"\nError: {MODEL_FILE} not found.")
        print("Run Day 33 first to create the saved model.")
        return

    if not os.path.exists(DATA_FILE):
        print(f"\nError: {DATA_FILE} not found.")
        return

    # Load model and data
    try:
        model = joblib.load(MODEL_FILE)
        data = pd.read_csv(DATA_FILE)
    except Exception as error:
        print("Could not load the model or dataset.")
        print("Details:", error)
        return

    required_columns = ["Deaths", "Assists", "Kills"]

    if not all(column in data.columns for column in required_columns):
        print("\nRequired columns:", required_columns)
        print("Available columns:", list(data.columns))
        return

    # Clean the required columns
    data = data[required_columns].copy()

    for column in required_columns:
        data[column] = pd.to_numeric(data[column], errors="coerce")

    data = data.dropna().reset_index(drop=True)

    if data.empty:
        print("No valid match data was found.")
        return

    # Predict kills using the saved model
    features = data[["Deaths", "Assists"]]
    actual_kills = data["Kills"].to_numpy()

    try:
        predicted_kills = model.predict(features)
    except Exception as error:
        print("Prediction failed. Check the model's input features.")
        print("Details:", error)
        return

    # Calculate prediction errors
    error_values = actual_kills - predicted_kills
    absolute_errors = abs(error_values)

    results = data.copy()
    results["Match_Number"] = range(1, len(results) + 1)
    results["Predicted_Kills"] = predicted_kills.round(2)
    results["Error"] = error_values.round(2)
    results["Absolute_Error"] = absolute_errors.round(2)

    # Label matches by prediction accuracy
    results["Error_Level"] = results["Absolute_Error"].apply(
        lambda error: (
            "Low" if error < 1
            else "Medium" if error < 3
            else "High"
        )
    )

    results.to_csv(REPORT_FILE, index=False)

    # Summary metrics
    mae = absolute_errors.mean()
    mse = (error_values ** 2).mean()
    rmse = mse ** 0.5

    print("\nERROR ANALYSIS SUMMARY")
    print("-" * 50)
    print(f"Matches analyzed: {len(results)}")
    print(f"Mean Absolute Error (MAE): {mae:.2f}")
    print(f"Mean Squared Error (MSE): {mse:.2f}")
    print(f"Root Mean Squared Error (RMSE): {rmse:.2f}")

    print("\nError Level Summary:")
    print(results["Error_Level"].value_counts().to_string())

    # Show matches with the largest errors
    print("\nMatches with the largest prediction errors:")
    worst_matches = results.nlargest(5, "Absolute_Error")

    print(
        worst_matches[
            [
                "Match_Number",
                "Kills",
                "Predicted_Kills",
                "Error",
                "Absolute_Error",
                "Error_Level"
            ]
        ].to_string(index=False)
    )

    # Plot actual and predicted kills
    plt.figure(figsize=(10, 6))
    match_numbers = results["Match_Number"]

    plt.plot(
        match_numbers,
        results["Kills"],
        marker="o",
        label="Actual Kills"
    )
    plt.plot(
        match_numbers,
        results["Predicted_Kills"],
        marker="s",
        linestyle="--",
        label="Predicted Kills"
    )

    plt.title("Day 36: Actual vs Predicted Kills")
    plt.xlabel("Match Number")
    plt.ylabel("Kills")
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig(CHART_FILE, dpi=150)
    plt.close()

    print("\nFiles created successfully:")
    print(f"1. {REPORT_FILE}")
    print(f"2. {CHART_FILE}")
    print("\nDay 36 completed!")


if __name__ == "__main__":
    main()
