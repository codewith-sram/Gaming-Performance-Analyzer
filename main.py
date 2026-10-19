
import pandas as pd
import matplotlib.pyplot as plt
import os

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error

print("========================================")
print("      GAMING PERFORMANCE ANALYZER")
print("========================================")

filename = "gaming_stats.csv"

if not os.path.exists(filename):
    print("Error: gaming_stats.csv was not found.")

else:
    df = pd.read_csv(filename)

    required = ["Match", "Kills", "Deaths", "Headshots", "Assists"]

    if not all(col in df.columns for col in required):
        print("Error: CSV must contain these columns:")
        print(required)

    else:
        # SELECT AND CLEAN REQUIRED DATA
        df = df[required].copy()

        for col in required:
            df[col] = pd.to_numeric(df[col], errors="coerce")

        df = df.dropna()
        df = df[
            (df["Kills"] >= 0)
            & (df["Deaths"] >= 0)
            & (df["Headshots"] >= 0)
            & (df["Assists"] >= 0)
        ]

        # CREATE NEW FEATURES
        df["KD_Ratio"] = (
            df["Kills"] / df["Deaths"].replace(0, float("nan"))
        ).fillna(0).round(2)

        df["Headshot_Rate"] = (
            df["Headshots"] / df["Kills"].replace(0, float("nan")) * 100
        ).fillna(0).round(2)

        print("\n===== FEATURE ENGINEERING =====")
        print(df[[
            "Match", "Kills", "Deaths", "Headshots",
            "Assists", "KD_Ratio", "Headshot_Rate"
        ]].to_string(index=False))

        # SAVE FEATURE-ENGINEERED DATA
        df.to_csv("gaming_features.csv", index=False)
        print("\nFeature data saved as gaming_features.csv")

        # USE GAMEPLAY FEATURES TO ESTIMATE KILLS
        # K/D and headshot rate are excluded because they use Kills
        # to calculate them, which would leak the answer to the model.
        features = ["Deaths", "Headshots", "Assists"]
        X = df[features]
        y = df["Kills"]

        if len(df) < 5:
            print("Add at least 5 valid match records to train and test.")
        else:
            X_train, X_test, y_train, y_test = train_test_split(
                X, y, test_size=0.2, random_state=42
            )

            model = RandomForestRegressor(
                n_estimators=100,
                random_state=42
            )

            model.fit(X_train, y_train)
            predictions = model.predict(X_test)

            mae = mean_absolute_error(y_test, predictions)
            rmse = mean_squared_error(y_test, predictions) ** 0.5

            results = pd.DataFrame({
                "Actual_Kills": y_test.values,
                "Predicted_Kills": predictions.round(2)
            })

            print("\n===== MODEL EVALUATION =====")
            print("Features used:", features)
            print("Training records:", len(X_train))
            print("Testing records:", len(X_test))
            print("Mean Absolute Error:", round(mae, 2))
            print("Root Mean Squared Error:", round(rmse, 2))

            print("\n===== ACTUAL VS PREDICTED =====")
            print(results.to_string(index=False))

            results.to_csv("day29_predictions.csv", index=False)

            # PLOT ACTUAL VS PREDICTED KILLS
            plt.figure(figsize=(8, 5))

            plt.scatter(
                y_test, predictions,
                label="Predictions"
            )

            lower = min(y_test.min(), predictions.min())
            upper = max(y_test.max(), predictions.max())

            plt.plot(
                [lower, upper], [lower, upper],
                linestyle="--",
                label="Perfect prediction"
            )

            plt.title("Day 29 - Actual vs Predicted Kills")
            plt.xlabel("Actual Kills")
            plt.ylabel("Predicted Kills")
            plt.legend()
            plt.grid(True, linestyle="--", alpha=0.5)
            plt.tight_layout()
            plt.savefig("day29_prediction_chart.png")

            print("\nPredictions saved as day29_predictions.csv")
            print("Chart saved as day29_prediction_chart.png")

            plt.show()

            print("\n========================================")
            print("          DAY 29 COMPLETED")
            print("========================================")
