
import pandas as pd
import matplotlib.pyplot as plt
import os

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error

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
    if not all(col in df.columns for col in ["Match", "Kills"]):
        print("Error: CSV must contain Match and Kills columns.")

    else:
        # CLEAN REQUIRED DATA
        df = df[["Match", "Kills"]].dropna()

        if len(df) < 5:
            print("Please provide at least 5 complete match records.")

        else:
            X = df[["Match"]]
            y = df["Kills"]

            # SPLIT DATA
            X_train, X_test, y_train, y_test = train_test_split(
                X,
                y,
                test_size=0.2,
                random_state=42
            )

            # CREATE TWO MODELS
            models = {
                "Linear Regression": LinearRegression(),
                "Decision Tree": DecisionTreeRegressor(
                    max_depth=2,
                    random_state=42
                )
            }

            results = []
            predictions = {}

            # TRAIN AND EVALUATE EACH MODEL
            for name, model in models.items():
                model.fit(X_train, y_train)
                y_pred = model.predict(X_test)

                mae = mean_absolute_error(y_test, y_pred)
                mse = mean_squared_error(y_test, y_pred)
                rmse = mse ** 0.5

                results.append({
                    "Model": name,
                    "MAE": round(mae, 2),
                    "RMSE": round(rmse, 2)
                })

                predictions[name] = y_pred

            # DISPLAY COMPARISON
            results_df = pd.DataFrame(results)

            print("\n===== MODEL COMPARISON =====")
            print(results_df.to_string(index=False))

            # SAVE COMPARISON TO CSV
            results_df.to_csv("model_comparison.csv", index=False)
            print("\nComparison saved as model_comparison.csv")

            # PLOT MODEL ERRORS
            plt.figure(figsize=(9, 5))

            plt.bar(
                results_df["Model"],
                results_df["MAE"]
            )

            plt.title("Model Comparison - Mean Absolute Error")
            plt.xlabel("Machine Learning Model")
            plt.ylabel("Mean Absolute Error (lower is better)")
            plt.grid(axis="y", linestyle="--", alpha=0.5)
            plt.tight_layout()

            plt.savefig("model_comparison.png")

            print("Chart saved as model_comparison.png")

            plt.show()

            # EXPLAIN THE RESULT
            best_model = results_df.loc[
                results_df["MAE"].idxmin(), "Model"
            ]

            print("\nModel with the lowest test MAE:", best_model)
            print("Lower MAE means smaller average absolute errors.")
            print("This small dataset is only for practice.")

            print("\n========================================")
            print("          DAY 28 COMPLETED")
            print("========================================")
