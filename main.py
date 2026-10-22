
import os
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import GridSearchCV, KFold
from sklearn.metrics import mean_absolute_error

print("========================================")
print("      GAMING PERFORMANCE ANALYZER")
print("========================================")

filename = "gaming_stats.csv"

# STEP 1: CHECK WHETHER THE CSV EXISTS
if not os.path.exists(filename):
    print("Error: gaming_stats.csv was not found.")
    print("Please run your Day 20 program first.")

else:
    # STEP 2: LOAD GAMING DATA
    df = pd.read_csv(filename)

    required_columns = ["Kills", "Deaths", "Assists"]

    if not all(column in df.columns for column in required_columns):
        print("Error: CSV must contain Kills, Deaths, and Assists.")

    else:
        # STEP 3: CLEAN DATA
        df = df[required_columns].copy()

        for column in required_columns:
            df[column] = pd.to_numeric(
                df[column], errors="coerce"
            )

        df = df.dropna()

        df = df[
            (df["Kills"] >= 0)
            & (df["Deaths"] >= 0)
            & (df["Assists"] >= 0)
        ]

        if len(df) < 5:
            print("Error: Please provide at least 5 valid match records.")

        else:
            # STEP 4: PREPARE FEATURES AND TARGET
            X = df[["Deaths", "Assists"]]
            y = df["Kills"]

            # STEP 5: DEFINE GRID SEARCH SETTINGS
            parameter_grid = {
                "n_estimators": [50, 100],
                "max_depth": [2, 3, None]
            }

            kfold = KFold(
                n_splits=5,
                shuffle=True,
                random_state=42
            )

            # STEP 6: RUN GRID SEARCH
            grid_search = GridSearchCV(
                estimator=RandomForestRegressor(
                    random_state=42
                ),
                param_grid=parameter_grid,
                scoring="neg_mean_absolute_error",
                cv=kfold,
                n_jobs=-1
            )

            print("\nTesting six model configurations...")
            grid_search.fit(X, y)

            # STEP 7: DISPLAY THE BEST SETTINGS
            print("\n===== BEST MODEL SETTINGS =====")
            print("Best parameters:", grid_search.best_params_)
            print(
                "Best cross-validation MAE:",
                round(-grid_search.best_score_, 2)
            )

            # STEP 8: PREPARE RESULTS
            results_df = pd.DataFrame(
                grid_search.cv_results_
            )

            results_df = pd.DataFrame({
                "Trees": results_df["param_n_estimators"].astype(int),
                "Max_Depth": results_df["param_max_depth"].astype(str),
                "Mean_MAE": -results_df["mean_test_score"],
                "Score_Std": results_df["std_test_score"],
                "Rank": results_df["rank_test_score"]
            })

            results_df["Mean_MAE"] = results_df["Mean_MAE"].round(3)
            results_df["Score_Std"] = results_df["Score_Std"].round(3)

            results_df = results_df.sort_values(
                "Rank"
            ).reset_index(drop=True)

            print("\n===== GRID SEARCH RESULTS =====")
            print(results_df.to_string(index=False))

            # STEP 9: SAVE RESULTS
            results_df.to_csv(
                "grid_search_results.csv",
                index=False
            )

            print("\nResults saved as grid_search_results.csv")

            # STEP 10: CREATE CHART
            # Convert labels and values to ordinary Python lists.
            chart_labels = [
                f"Trees={trees}\nDepth={depth}"
                for trees, depth in zip(
                    results_df["Trees"].tolist(),
                    results_df["Max_Depth"].tolist()
                )
            ]

            chart_values = results_df["Mean_MAE"].astype(float).tolist()

            plt.figure(figsize=(10, 6))

            plt.bar(
                range(len(chart_labels)),
                chart_values,
                tick_label=chart_labels
            )

            plt.title("Grid Search - Random Forest Settings")
            plt.xlabel("Model Settings")
            plt.ylabel("Cross-Validation MAE (lower is better)")
            plt.xticks(rotation=30, ha="right")
            plt.grid(axis="y", linestyle="--", alpha=0.5)
            plt.tight_layout()

            # SAVE CHART
            plt.savefig(
                "grid_search_comparison.png",
                dpi=150,
                bbox_inches="tight"
            )

            print("Chart saved as grid_search_comparison.png")

            # STEP 11: DISPLAY CHART
            plt.show()

            # STEP 12: FINISH
            print("\n========================================")
            print("          DAY 32 COMPLETED")
            print("========================================")
