import pandas as pd
import matplotlib.pyplot as plt
import os

from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error

print("========================================")
print("      GAMING PERFORMANCE ANALYZER")
print("========================================")

filename = "gaming_stats.csv"

if not os.path.exists(filename):
    print("Error: gaming_stats.csv was not found.")
    print("Run your Day 20 program first.")

else:
    df = pd.read_csv(filename)

    # CHECK REQUIRED COLUMNS
    required = ["Kills", "Deaths", "Assists"]

    if not all(column in df.columns for column in required):
        print("Error: CSV must contain Kills, Deaths, and Assists.")

    else:
        # CLEAN DATA
        df = df[required].copy()

        for column in required:
            df[column] = pd.to_numeric(df[column], errors="coerce")

        df = df.dropna()
        df = df[
            (df["Kills"] >= 0)
            & (df["Deaths"] >= 0)
            & (df["Assists"] >= 0)
        ]

        if len(df) < 5:
            print("Please provide at least 5 valid match records.")

        else:
            # INPUT FEATURES AND TARGET
            # Do not use Headshots or K/D here because they depend on Kills.
            X = df[["Deaths", "Assists"]]
            y = df["Kills"]

            # SPLIT DATA
            X_train, X_test, y_train, y_test = train_test_split(
                X,
                y,
                test_size=0.2,
                random_state=42
            )

            # TRAIN MODEL
            model = RandomForestRegressor(
                n_estimators=100,
                random_state=42
            )

            model.fit(X_train, y_train)

            # EVALUATE MODEL
            predictions = model.predict(X_test)
            mae = mean_absolute_error(y_test, predictions)

            print("\n===== MODEL EVALUATION =====")
            print("Training records:", len(X_train))
            print("Testing records:", len(X_test))
            print("Mean Absolute Error:", round(mae, 2))

            # CALCULATE FEATURE IMPORTANCE
            importance_df = pd.DataFrame({
                "Feature": X.columns,
                "Importance": model.feature_importances_
            })

            importance_df = importance_df.sort_values(
                "Importance",
                ascending=False
            )

            print("\n===== FEATURE IMPORTANCE =====")
            print(importance_df.to_string(index=False))

            # SAVE IMPORTANCE RESULTS
            importance_df.to_csv(
                "feature_importance.csv",
                index=False
            )

            print("\nResults saved as feature_importance.csv")

            # CREATE FEATURE IMPORTANCE CHART
            plt.figure(figsize=(8, 5))

            plt.bar(
                importance_df["Feature"],
                importance_df["Importance"]
            )

            plt.title("Gaming Performance - Feature Importance")
            plt.xlabel("Gaming Feature")
            plt.ylabel("Relative Importance")
            plt.grid(axis="y", linestyle="--", alpha=0.5)
            plt.tight_layout()

            plt.savefig("feature_importance.png")

            print("Chart saved as feature_importance.png")

            plt.show()

            print("\n========================================")
            print("          DAY 30 COMPLETED")
            print("========================================")