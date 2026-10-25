
import os
import joblib
import pandas as pd
import matplotlib.pyplot as plt

MODEL_FILE = "gaming_model.pkl"
DATA_FILE = "gaming_stats.csv"
REPORT_FILE = "day35_model_evaluation.csv"
CHART_FILE = "day35_model_evaluation.png"


def main():
    print("=" * 45)
    print(" GAMING PERFORMANCE ANALYZER - DAY 35")
    print(" Model Evaluation System")
    print("=" * 45)

    # Check required files
    if not os.path.exists(MODEL_FILE):
        print(f"\nError: {MODEL_FILE} not found.")
        print("Run Day 33 first to create the saved model.")
        return

    if not os.path.exists(DATA_FILE):
        print(f"\nError: {DATA_FILE} not found.")
        print("Make sure your gaming dataset is in this folder.")
        return

    # Load the saved model and gaming dataset
    try:
        model = joblib.load(MODEL_FILE)
        data = pd.read_csv(DATA_FILE)
    except Exception as error:
        print("Could not load the model or dataset.")
        print("Details:", error)
        return

    required_columns = ["Deaths", "Assists", "Kills"]

    if not all(column in data.columns for column in required_columns):
        print("\nError: The dataset must contain these columns:")
        print(", ".join(required_columns))
        print("\nAvailable columns:", list(data.columns))
        return

    # Keep only required columns and clean invalid values
    data = data[required_columns].copy()

    for column in required_columns:
        data[column] = pd.to_numeric(data[column], errors="coerce")

    data = data.dropna()

    if len(data) < 2:
        print("At least two valid matches are required.")
        return

    # Use the same features as the Day 33 model
    X = data[["Deaths", "Assists"]]
    actual_kills = data["Kills"]

    try:
        predicted_kills = model.predict(X)
    except Exception as error:
        print("Prediction failed. Check your Day 33 model features.")
        print("Details:", error)
        return

    # Calculate evaluation metrics
    errors = actual_kills.to_numpy() - predicted_kills
    mae = abs(errors).mean()
    mse = (errors ** 2).mean()
    rmse = mse ** 0.5

    results = data.copy()
    results["Predicted_Kills"] = predicted_kills
    results["Prediction_Error"] = errors
    results["Absolute_Error"] = abs(errors)

    results.to_csv(REPORT_FILE, index=False)

    print("\nMODEL EVALUATION RESULTS")
    print("-" * 45)
    print(f"Matches evaluated: {len(results)}")
    print(f"Mean Absolute Error (MAE): {mae:.2f}")
    print(f"Mean Squared Error (MSE): {mse:.2f}")
    print(f"Root Mean Squared Error (RMSE): {rmse:.2f}")

    print("\nFirst five evaluation results:")
    print(results.head().round(2).to_string(index=False))

    # Create an actual-versus-predicted chart
    plt.figure(figsize=(9, 5))
    match_numbers = range(1, len(results) + 1)

    plt.plot(
        match_numbers,
        actual_kills,
        marker="o",
        label="Actual Kills"
    )
    plt.plot(
        match_numbers,
        predicted_kills,
        marker="s",
        linestyle="--",
        label="Predicted Kills"
    )

    plt.title("Actual vs Predicted Kills")
    plt.xlabel("Match Number")
    plt.ylabel("Kills")
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig(CHART_FILE, dpi=150)
    plt.close()

    print("\nFiles created:")
    print(f"1. {REPORT_FILE}")
    print(f"2. {CHART_FILE}")
    print("\nDay 35 completed!")


if __name__ == "__main__":
    main()
