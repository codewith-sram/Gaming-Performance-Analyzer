import pandas as pd
import matplotlib.pyplot as plt
import os

from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import KFold, cross_val_score

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

    required_columns = ["Kills", "Deaths", "Assists"]

    if not all(col in df.columns for col in required_columns):
        print("Error: CSV must contain Kills, Deaths, and Assists.")

    else:
        # CLEAN DATA
        df = df[required_columns].copy()

        for col in required_columns:
            df[col] = pd.to_numeric(df[col], errors="coerce")

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
            X = df[["Deaths", "Assists"]]
            y = df["Kills"]

            # CREATE MODEL
            model = RandomForestRegressor(
                n_estimators=100,
                random_state=42
            )

            # CREATE 5-FOLD CROSS-VALIDATION
            kfold = KFold(
                n_splits=5,
                shuffle=True,
                random_state=42
            )

            # CALCULATE MAE FOR EACH FOLD
            scores = cross_val_score(
                model,
                X,
                y,
                cv=kfold,
                scoring="neg_mean_absolute_error"
            )

            # CONVERT NEGATIVE MAE TO POSITIVE VALUES
            mae_scores = -scores

            results_df = pd.DataFrame({
                "Fold": range(1, len(mae_scores) + 1),
                "MAE": mae_scores.round(2)
            })

            average_mae = mae_scores.mean()
            std_mae = mae_scores.std()

            print("\n===== 5-FOLD CROSS-VALIDATION =====")
            print(results_df.to_string(index=False))

            print("\nAverage MAE:", round(average_mae, 2))
            print("MAE standard deviation:", round(std_mae, 2))

            # SAVE RESULTS
            results_df.to_csv(
                "cross_validation_results.csv",
                index=False
            )

            print("\nResults saved as cross_validation_results.csv")

            # CREATE CHART
            plt.figure(figsize=(9, 5))

            plt.bar(
                results_df["Fold"],
                results_df["MAE"]
            )

            plt.axhline(
                y=average_mae,
                linestyle="--",
                label=f"Average MAE: {average_mae:.2f}"
            )

            plt.title("Day 31 - Cross-Validation Results")
            plt.xlabel("Fold Number")
            plt.ylabel("Mean Absolute Error (lower is better)")
            plt.xticks(results_df["Fold"])
            plt.legend()
            plt.grid(axis="y", linestyle="--", alpha=0.5)
            plt.tight_layout()

            plt.savefig("cross_validation.png")

            print("Chart saved as cross_validation.png")

            plt.show()

            print("\n========================================")
            print("          DAY 31 COMPLETED")
            print("========================================")