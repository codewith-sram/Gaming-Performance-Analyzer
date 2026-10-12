
import pandas as pd
import matplotlib.pyplot as plt
import os

print("========================================")
print("      GAMING PERFORMANCE ANALYZER")
print("========================================")

# CSV FILE
filename = "gaming_stats.csv"

if not os.path.exists(filename):
    print("Error: gaming_stats.csv was not found.")
    print("Run your Day 20 program first to create the CSV file.")

else:
    # LOAD GAMING DATA
    df = pd.read_csv(filename)

    print("\n===== GAMING STATISTICS =====")
    print(df)

    # CALCULATE PERFORMANCE
    total_kills = df["Kills"].sum()
    average_kills = df["Kills"].mean()

    print("\nTotal kills:", total_kills)
    print("Average kills:", round(average_kills, 2))

    # CREATE LINE CHART
    plt.figure(figsize=(9, 5))

    plt.plot(
        df["Match"],
        df["Kills"],
        marker="o",
        linestyle="-",
        label="Kills per Match"
    )

    # SHOW AVERAGE KILLS AS A REFERENCE LINE
    plt.axhline(
        y=average_kills,
        linestyle="--",
        label="Average Kills"
    )

    # CHART DETAILS
    plt.title("Gaming Performance Trend")
    plt.xlabel("Match Number")
    plt.ylabel("Number of Kills")
    plt.xticks(df["Match"])
    plt.legend()
    plt.grid(True, linestyle="--", alpha=0.5)

    # SAVE CHART
    plt.tight_layout()
    plt.savefig("kills_trend.png")

    print("\nLine chart saved as kills_trend.png")

    # DISPLAY CHART
    plt.show()

    print("\n========================================")
    print("          DAY 22 COMPLETED")
    print("========================================")
