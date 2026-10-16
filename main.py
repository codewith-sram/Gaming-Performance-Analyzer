
import pandas as pd
import matplotlib.pyplot as plt
import os
from sklearn.linear_model import LinearRegression

print("========================================")
print("      GAMING PERFORMANCE ANALYZER")
print("========================================")

filename = "gaming_stats.csv"

# CHECK CSV FILE
if not os.path.exists(filename):
    print("Error: gaming_stats.csv was not found.")
    print("Run your Day 20 program first.")

else:
    # LOAD GAMING DATA
    df = pd.read_csv(filename)

    # CHECK REQUIRED DATA
    required_columns = ["Match", "Kills"]

    if not all(column in df.columns for column in required_columns):
        print("Error: CSV must contain Match and Kills columns.")

    elif len(df) < 2:
        print("Please add at least two match records.")

    else:
        # PREPARE DATA FOR MACHINE LEARNING
        X = df[["Match"]]
        y = df["Kills"]

        # CREATE THE MODEL
        model = LinearRegression()

        # TRAIN THE MODEL
        model.fit(X, y)

        # PREDICT KILLS FOR THE NEXT MATCH
        next_match = int(df["Match"].max()) + 1
        prediction = model.predict(
            pd.DataFrame({"Match": [next_match]})
        )[0]

        print("\n===== MACHINE LEARNING RESULTS =====")
        print("Training matches:", len(df))
        print("Model: Linear Regression")
        print("Next match number:", next_match)
        print("Predicted kills:", round(max(0, prediction), 2))

        # SHOW ACTUAL DATA AND PREDICTION
        plt.figure(figsize=(9, 5))

        plt.scatter(
            df["Match"], df["Kills"],
            label="Actual Kills"
        )

        plt.plot(
            df["Match"], model.predict(X),
            label="Regression Line"
        )

        plt.scatter(
            [next_match], [max(0, prediction)],
            marker="X", s=120,
            label="Predicted Kills"
        )

        plt.title("Gaming Kills Prediction - Linear Regression")
        plt.xlabel("Match Number")
        plt.ylabel("Kills")
        plt.legend()
        plt.grid(True, linestyle="--", alpha=0.5)
        plt.tight_layout()

        plt.savefig("kills_prediction.png")

        print("\nChart saved as kills_prediction.png")

        plt.show()

        print("\n========================================")
        print("          DAY 26 COMPLETED")
        print("========================================")
