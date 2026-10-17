
import pandas as pd
import matplotlib.pyplot as plt
import os
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error
import math

print("========================================")
print("      GAMING PERFORMANCE ANALYZER")
print("========================================")

filename = "gaming_stats.csv"

if not os.path.exists(filename):
    print("Error: gaming_stats.csv was not found.")
    print("Run your Day 20 program first.")

else:
    # LOAD DATA
    df = pd.read_csv(filename)

    # KEEP REQUIRED COLUMNS AND REMOVE MISSING VALUES
    required_columns = ["Match", "Kills"]

    if not all(column in df.columns for column in required_columns):
        print("Error: CSV must contain Match and Kills columns.")

    else:
        df = df[["Match", "Kills"]].dropna()

        if len(df) < 5:
            print("Please provide at least 5 complete match records.")

        else:
            # INPUT AND OUTPUT
            X = df[["Match"]]
            y = df["Kills"]

            # SPLIT INTO TRAINING AND TESTING DATA
            X_train, X_test, y_train, y_test = train_test_split(
                X,
                y,
                test_size=0.2,
                random_state=42
            )

            print("\n===== DATA SPLIT =====")
            print("Total records:", len(df))
            print("Training records:", len(X_train))
            print("Testing records:", len(X_test))

            # CREATE AND TRAIN MODEL
            model = LinearRegression()
            model.fit(X_train, y_train)

            # PREDICT TEST DATA
            y_pred = model.predict(X_test)

            # CALCULATE ERROR METRICS
            mae = mean_absolute_error(y_test, y_pred)
            mse = mean_squared_error(y_test, y_pred)
            rmse = math.sqrt(mse)

            print("\n===== MODEL EVALUATION =====")
            print("Mean Absolute Error (MAE):", round(mae, 2))
            print("Mean Squared Error (MSE):", round(mse, 2))
            print("Root Mean Squared Error (RMSE):", round(rmse, 2))

            # DISPLAY ACTUAL AND PREDICTED RESULTS
            results = pd.DataFrame({
                "Match": X_test["Match"].values,
                "Actual Kills": y_test.values,
                "Predicted Kills": y_pred.round(2)
            })

            results = results.sort_values("Match")

            print("\n===== ACTUAL VS PREDICTED =====")
            print(results.to_string(index=False))

            # PLOT TEST RESULTS
            plt.figure(figsize=(9, 5))

            plt.plot(
                results["Match"],
                results["Actual Kills"],
                marker="o",
                label="Actual Kills"
            )

            plt.plot(
                results["Match"],
                results["Predicted Kills"],
                marker="s",
                linestyle="--",
                label="Predicted Kills"
            )

            plt.title("Day 27 - Model Testing Results")
            plt.xlabel("Match Number")
            plt.ylabel("Kills")
            plt.legend()
            plt.grid(True, linestyle="--", alpha=0.5)
            plt.tight_layout()

            # SAVE RESULTS AND CHART
            results.to_csv("model_test_results.csv", index=False)
            plt.savefig("model_testing.png")

            print("\nResults saved as model_test_results.csv")
            print("Chart saved as model_testing.png")

            plt.show()

            print("\n========================================")
            print("          DAY 27 COMPLETED")
            print("========================================")
