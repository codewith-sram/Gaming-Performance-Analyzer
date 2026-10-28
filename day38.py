import os
import pandas as pd
import matplotlib.pyplot as plt

DATA_FILE = "gaming_stats.csv"
REPORT_FILE = "day38_performance_report.csv"
CHART_FILE = "day38_performance_dashboard.png"


def main():
    print("=" * 50)
    print(" GAMING PERFORMANCE ANALYZER - DAY 38")
    print(" Performance Dashboard and Report")
    print("=" * 50)

    # Check whether the dataset exists
    if not os.path.exists(DATA_FILE):
        print(f"\nError: {DATA_FILE} was not found.")
        print("Place the CSV file in your project folder.")
        return

    try:
        data = pd.read_csv(DATA_FILE)
    except Exception as error:
        print("Could not read the dataset:", error)
        return

    # Check the required columns
    required_columns = ["Kills", "Deaths", "Assists"]

    if not all(column in data.columns for column in required_columns):
        print("\nYour CSV must contain these columns:")
        print("Kills, Deaths, Assists")
        print("Available columns:", list(data.columns))
        return

    # Clean the data
    for column in required_columns:
        data[column] = pd.to_numeric(data[column], errors="coerce")

    data = data.dropna(subset=required_columns).reset_index(drop=True)

    if data.empty:
        print("No valid gaming records found.")
        return

    # Calculate performance statistics
    total_matches = len(data)
    total_kills = data["Kills"].sum()
    total_deaths = data["Deaths"].sum()
    total_assists = data["Assists"].sum()

    average_kills = data["Kills"].mean()
    average_deaths = data["Deaths"].mean()
    average_assists = data["Assists"].mean()

    if total_deaths > 0:
        kd_ratio = total_kills / total_deaths
    else:
        kd_ratio = None

    # Create a report
    report = pd.DataFrame([{
        "Total_Matches": total_matches,
        "Total_Kills": total_kills,
        "Total_Deaths": total_deaths,
        "Total_Assists": total_assists,
        "Average_Kills": round(average_kills, 2),
        "Average_Deaths": round(average_deaths, 2),
        "Average_Assists": round(average_assists, 2),
        "Overall_KD_Ratio": round(kd_ratio, 2)
        if kd_ratio is not None else "Undefined"
    }])

    report.to_csv(REPORT_FILE, index=False)

    # Display the report
    print("\nPERFORMANCE SUMMARY")
    print("-" * 50)
    print(f"Total matches: {total_matches}")
    print(f"Total kills: {total_kills:g}")
    print(f"Total deaths: {total_deaths:g}")
    print(f"Total assists: {total_assists:g}")
    print(f"Average kills: {average_kills:.2f}")
    print(f"Average deaths: {average_deaths:.2f}")
    print(f"Average assists: {average_assists:.2f}")

    if kd_ratio is not None:
        print(f"Overall K/D ratio: {kd_ratio:.2f}")
    else:
        print("Overall K/D ratio: Undefined (zero deaths)")

    # Create a four-panel dashboard
    match_numbers = range(1, total_matches + 1)

    fig, axes = plt.subplots(2, 2, figsize=(12, 8))

    # Chart 1: Kills by match
    axes[0, 0].bar(match_numbers, data["Kills"])
    axes[0, 0].set_title("Kills per Match")
    axes[0, 0].set_xlabel("Match Number")
    axes[0, 0].set_ylabel("Kills")

    # Chart 2: Deaths by match
    axes[0, 1].bar(match_numbers, data["Deaths"])
    axes[0, 1].set_title("Deaths per Match")
    axes[0, 1].set_xlabel("Match Number")
    axes[0, 1].set_ylabel("Deaths")

    # Chart 3: Kills, deaths and assists
    axes[1, 0].plot(
        match_numbers, data["Kills"], marker="o", label="Kills"
    )
    axes[1, 0].plot(
        match_numbers, data["Deaths"], marker="s", label="Deaths"
    )
    axes[1, 0].plot(
        match_numbers, data["Assists"], marker="^", label="Assists"
    )
    axes[1, 0].set_title("Match Performance Comparison")
    axes[1, 0].set_xlabel("Match Number")
    axes[1, 0].set_ylabel("Count")
    axes[1, 0].legend()

    # Chart 4: Average performance
    categories = ["Kills", "Deaths", "Assists"]
    averages = [
        average_kills, average_deaths, average_assists
    ]

    axes[1, 1].bar(categories, averages)
    axes[1, 1].set_title("Average Performance")
    axes[1, 1].set_ylabel("Average Count")

    fig.suptitle("Gaming Performance Dashboard", fontsize=16)
    fig.tight_layout()
    fig.savefig(CHART_FILE, dpi=150)
    plt.close(fig)

    print("\nFiles created successfully:")
    print(f"1. {REPORT_FILE}")
    print(f"2. {CHART_FILE}")
    print("\nDay 38 completed!")


if __name__ == "__main__":
    main()