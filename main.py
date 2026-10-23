
import os
import pandas as pd
import joblib

from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import GridSearchCV, KFold

print("========================================")
print("      GAMING PERFORMANCE ANALYZER")
print("========================================")

filename = "gaming_stats.csv"
model_file = "gaming_model.pkl"

# STEP 1: CHECK THE CSV FILE
if not os.path.exists(filename):
    print("Error: gaming_stats.csv was not found.")
    print("Please run your Day 20 program first.")

else:
    df = pd.read_csv(filename)

    required_columns = ["Kills", "Deaths", "Assists"]

    if not all(col in df.columns for col in required_columns):
        print("Error: CSV must contain Kills, Deaths, and Assists.")

    else:
        # STEP 2: CLEAN DATA
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
            # STEP 3: PREPARE FEATURES AND TARGET
            X = df[["Deaths", "Assists"]]
            y = df["Kills"]

            # STEP 4: FIND GOOD MODEL SETTINGS
            parameter_grid = {
                "n_estimators": [50, 100],
                "max_depth": [2, 3, None]
            }

            kfold = KFold(
                n_splits=5,
                shuffle=True,
                random_state=42
            )

            grid_search = GridSearchCV(
                estimator=RandomForestRegressor(random_state=42),
                param_grid=parameter_grid,
                scoring="neg_mean_absolute_error",
                cv=kfold,
                n_jobs=-1
            )

            print("\nTraining the model...")
            grid_search.fit(X, y)

            best_model = grid_search.best_estimator_

            print("Best settings:", grid_search.best_params_)
            print(
                "Cross-validation MAE:",
                round(-grid_search.best_score_, 2)
            )

            # STEP 5: SAVE THE TRAINED MODEL
            joblib.dump(best_model, model_file)

            print("\nModel saved as", model_file)

            # STEP 6: LOAD THE SAVED MODEL
            loaded_model = joblib.load(model_file)

            print("Saved model loaded successfully!")

            # STEP 7: ASK FOR NEW MATCH STATISTICS
            print("\n===== PREDICT YOUR NEXT MATCH =====")

            try:
                deaths = float(input("Enter expected deaths: "))
                assists = float(input("Enter expected assists: "))

                if deaths < 0 or assists < 0:
                    print("Deaths and assists cannot be negative.")

                else:
                    # KEEP INPUT FORMAT THE SAME AS TRAINING
                    new_match = pd.DataFrame({
                        "Deaths": [deaths],
                        "Assists": [assists]
                    })

                    prediction = loaded_model.predict(new_match)[0]
                    prediction = max(0, prediction)

                    print(
                        "\nPredicted kills:",
                        round(prediction, 2)
                    )

                    # STEP 8: SAVE PREDICTION
                    prediction_data = pd.DataFrame({
                        "Deaths": [deaths],
                        "Assists": [assists],
                        "Predicted_Kills": [round(prediction, 2)]
                    })

                    output_file = "gaming_prediction.csv"

                    if os.path.exists(output_file):
                        old_data = pd.read_csv(output_file)
                        prediction_data = pd.concat(
                            [old_data, prediction_data],
                            ignore_index=True
                        )

                    prediction_data.to_csv(
                        output_file,
                        index=False
                    )

                    print("Prediction saved to", output_file)

            except ValueError:
                print("Please enter valid numeric values.")

            print("\n========================================")
            print("          DAY 33 COMPLETED")
            print("========================================")
