
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
    print("Please run your Day 20 program first.")

else:
    # LOAD DATA
    df = pd.read_csv(filename)

    # CHECK REQUIRED COLUMNS
    required_columns = ["Match", "Kills", "Deaths", "Assists"]
    missing_columns = [
        column for column in required_columns
        if column not in df.columns
    ]

    if missing_columns:
        print("CSV is missing these columns:", missing_columns)

    elif df.empty:
        print("The CSV file contains no gaming records.")

    else:
        # CALCULATE STATISTICS
        total_kills = df["Kills"].sum()
        total_deaths = df["Deaths"].sum()
        total_assists = df["Assists"].sum()
        average_kills = df["Kills"].mean()

        print("\n===== PLAYER PERFORMANCE SUMMARY =====")
        print("Total matches:", len(df))
        print("Total kills:", total_kills)
        print("Total deaths:", total_deaths)
        print("Total assists:", total_assists)
        print("Average kills:", round(average_kills, 2))

        # CREATE DASHBOARD WITH FOUR PANELS
        fig, axes = plt.subplots(2, 2, figsize=(12, 8))

        fig.suptitle(
            "GAMING PERFORMANCE DASHBOARD",
            fontsize=16
        )

        # PANEL 1: KILLS BAR CHART
        axes[0, 0].bar(df["Match"], df["Kills"])
        axes[0, 0].set_title("Kills Per Match")
        axes[0, 0].set_xlabel("Match")
        axes[0, 0].set_ylabel("Kills")
        axes[0, 0].grid(axis="y", linestyle="--", alpha=0.4)

        # PANEL 2: PERFORMANCE LINE CHART
        axes[0, 1].plot(
            df["Match"], df["Kills"],
            marker="o", label="Kills"
        )
        axes[0, 1].plot(
            df["Match"], df["Deaths"],
            marker="s", label="Deaths"
        )
        axes[0, 1].plot(
            df["Match"], df["Assists"],
            marker="^", label="Assists"
        )
        axes[0, 1].set_title("Match Performance")
        axes[0, 1].set_xlabel("Match")
        axes[0, 1].set_ylabel("Count")
        axes[0, 1].legend()
        axes[0, 1].grid(True, linestyle="--", alpha=0.4)

        # PANEL 3: STATISTICS PIE CHART
        labels = ["Kills", "Deaths", "Assists"]
        values = [total_kills, total_deaths, total_assists]

        if sum(values) > 0:
            axes[1, 0].pie(
                values,
                labels=labels,
                autopct="%1.1f%%",
                startangle=90
            )
            axes[1, 0].set_title("Statistics Distribution")
        else:
            axes[1, 0].text(
                0.5, 0.5, "No data to display",
                ha="center", va="center"
            )
            axes[1, 0].set_title("Statistics Distribution")

        # PANEL 4: SUMMARY
        axes[1, 1].axis("off")
        summary = (
            "PERFORMANCE SUMMARY\n\n"
            f"Total Matches: {len(df)}\n"
            f"Total Kills: {total_kills}\n"
            f"Total Deaths: {total_deaths}\n"
            f"Total Assists: {total_assists}\n"
            f"Average Kills: {average_kills:.2f}"
        )

        axes[1, 1].text(
            0.1, 0.85, summary,
            fontsize=13,
            va="top",
            linespacing=1.6
        )

        # SAVE AND DISPLAY DASHBOARD
        plt.tight_layout(rect=[0, 0, 1, 0.95])
        plt.savefig("gaming_dashboard.png", dpi=150)

        print("\nDashboard saved as gaming_dashboard.png")

        plt.show()

        print("\n========================================")
        print("          DAY 25 COMPLETED")
        print("========================================")
