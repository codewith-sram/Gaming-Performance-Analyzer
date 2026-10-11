
import pandas as pd
import matplotlib.pyplot as plt
import os

print("========================================")
print("      GAMING PERFORMANCE ANALYZER")
print("========================================")

# CHECK WHETHER THE CSV FILE EXISTS
filename = "gaming_stats.csv"

if not os.path.exists(filename):
    print("Error: gaming_stats.csv was not found.")
    print("Run your Day 20 program first to create the CSV file.")
else:
    # LOAD GAMING DATA
    df = pd.read_csv(filename)

    print("\n===== GAMING STATISTICS =====")
    print(df)

    # CALCULATE TOTAL AND AVERAGE KILLS
    total_kills = df["Kills"].sum()
    average_kills = df["Kills"].mean()

    print("\nTotal kills:", total_kills)
    print("Average kills:", round(average_kills, 2))

    # CREATE A BAR CHART
    plt.figure(figsize=(9, 5))

    plt.bar(
        df["Match"],
        df["Kills"],
        label="Kills"
    )

    # ADD CHART DETAILS
    plt.title("Gaming Performance - Kills Per Match")
    plt.xlabel("Match Number")
    plt.ylabel("Number of Kills")
    plt.xticks(df["Match"])
    plt.legend()
    plt.grid(axis="y", linestyle="--", alpha=0.5)

    # SAVE THE CHART
    plt.tight_layout()
    plt.savefig("kills_per_match.png")

    print("\nChart saved as kills_per_match.png")

    # DISPLAY THE CHART
    plt.show()

    print("\n========================================")
    print("          DAY 21 COMPLETED")
    print("========================================")
