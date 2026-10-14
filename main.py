
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

    # PREPARE PIE CHART DATA
    labels = ["Kills", "Deaths", "Assists"]
    values = [total_kills, total_deaths, total_assists]

    # CREATE PIE CHART
    plt.figure(figsize=(8, 8))

    plt.pie(
        values,
        labels=labels,
        autopct="%1.1f%%",
        startangle=90
    )

    plt.title("Distribution of Gaming Statistics")
    plt.axis("equal")

    # SAVE CHART
    plt.tight_layout()
    plt.savefig("gaming_distribution.png")

    print("\nPie chart saved as gaming_distribution.png")

    # DISPLAY CHART
    plt.show()

    print("\n========================================")
    print("          DAY 24 COMPLETED")
    print("========================================")
