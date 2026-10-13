
import pandas as pd
import matplotlib.pyplot as plt
import os

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

    print("\n===== GAMING STATISTICS =====")
    print(df)

    # CALCULATE TOTALS
    total_kills = df["Kills"].sum()
    total_deaths = df["Deaths"].sum()
    total_assists = df["Assists"].sum()

    print("\n===== TOTAL STATISTICS =====")
    print("Total kills:", total_kills)
    print("Total deaths:", total_deaths)
    print("Total assists:", total_assists)

    # CREATE MULTI-LINE CHART
    plt.figure(figsize=(10, 6))

    plt.plot(
        df["Match"], df["Kills"],
        marker="o", label="Kills"
    )

    plt.plot(
        df["Match"], df["Deaths"],
        marker="s", label="Deaths"
    )

    plt.plot(
        df["Match"], df["Assists"],
        marker="^", label="Assists"
    )

    # ADD CHART DETAILS
    plt.title("Gaming Statistics Comparison")
    plt.xlabel("Match Number")
    plt.ylabel("Count")
    plt.xticks(df["Match"])
    plt.legend()
    plt.grid(True, linestyle="--", alpha=0.5)

    # SAVE CHART
    plt.tight_layout()
    plt.savefig("gaming_comparison.png")

    print("\nChart saved as gaming_comparison.png")

    # DISPLAY CHART
    plt.show()

    print("\n========================================")
    print("          DAY 23 COMPLETED")
    print("========================================")
