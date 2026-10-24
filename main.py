
import os
import joblib
import pandas as pd

MODEL_FILE = "gaming_model.pkl"
PREDICTIONS_FILE = "day34_predictions.csv"
HISTORY_FILE = "prediction_history.csv"


def main():
    print("=" * 45)
    print(" GAMING PERFORMANCE ANALYZER - DAY 34")
    print(" Saved Model Prediction System")
    print("=" * 45)

    # Check whether the Day 33 model exists
    if not os.path.exists(MODEL_FILE):
        print(f"\nError: {MODEL_FILE} was not found.")
        print("Run your Day 33 program first to create the saved model.")
        return

    # Load the saved model without training again
    try:
        model = joblib.load(MODEL_FILE)
    except Exception as error:
        print("Could not load the saved model.")
        print("Details:", error)
        return

    print("\nSaved model loaded successfully!")

    try:
        number_of_matches = int(
            input("\nHow many matches do you want to predict? ")
        )

        if number_of_matches <= 0:
            print("Please enter a number greater than zero.")
            return

        match_data = []

        for match_number in range(1, number_of_matches + 1):
            print(f"\n--- Match {match_number} ---")

            deaths = int(input("Enter deaths: "))
            assists = int(input("Enter assists: "))

            if deaths < 0 or assists < 0:
                print("Deaths and assists cannot be negative.")
                return

            match_data.append({
                "Deaths": deaths,
                "Assists": assists
            })

    except ValueError:
        print("Invalid input. Please enter whole numbers.")
        return

    # Create a DataFrame with the same features used in Day 33
    input_data = pd.DataFrame(
        match_data,
        columns=["Deaths", "Assists"]
    )

    try:
        predicted_kills = model.predict(input_data)
    except Exception as error:
        print("\nPrediction failed. Check that the Day 33 model")
        print("was trained using the features Deaths and Assists.")
        print("Details:", error)
        return

    # Prepare the prediction results
    results = input_data.copy()
    results.insert(
        0,
        "Match",
        range(1, number_of_matches + 1)
    )
    results["Predicted_Kills"] = (
        pd.Series(predicted_kills).round(0).astype(int).values
    )

    # Save this session's predictions
    results.to_csv(PREDICTIONS_FILE, index=False)

    # Add predictions to the history file
    results["Prediction_Date"] = pd.Timestamp.now().strftime(
        "%Y-%m-%d %H:%M:%S"
    )

    if os.path.exists(HISTORY_FILE):
        results.to_csv(
            HISTORY_FILE,
            mode="a",
            header=False,
            index=False
        )
    else:
        results.to_csv(HISTORY_FILE, index=False)

    print("\n" + "=" * 45)
    print(" PREDICTION RESULTS")
    print("=" * 45)
    print(results.to_string(index=False))

    print("\nFiles saved successfully:")
    print(f"1. {PREDICTIONS_FILE}")
    print(f"2. {HISTORY_FILE}")
    print("\nDay 34 completed!")


if __name__ == "__main__":
    main()
