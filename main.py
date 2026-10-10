
import pandas as pd
import os

print("========================================")
print("      GAMING PERFORMANCE ANALYZER")
print("========================================")

# PLAYER INFORMATION
player_name = input("Enter player name: ")
game_name = input("Enter game name: ")

# GAMING DATA
data = {
    "Match": [1, 2, 3, 4, 5],
    "Kills": [12, 15, 8, 20, 10],
    "Deaths": [6, 5, 4, 5, 5],
    "Headshots": [5, 7, 3, 9, 4],
    "Assists": [3, 4, 2, 5, 3]
}

# CREATE DATAFRAME
df = pd.DataFrame(data)

# CALCULATE K/D RATIO
df["K/D"] = (
    df["Kills"] /
    df["Deaths"].replace(0, float("nan"))
).fillna(0).round(2)

print("\n===== GAMING STATISTICS =====")
print(df)

# SAVE DATA TO CSV
filename = "gaming_stats.csv"
df.to_csv(filename, index=False)

print("\nStatistics saved successfully!")
print("File name:", filename)

# CHECK WHETHER FILE EXISTS
if os.path.exists(filename):
    print("CSV file exists.")

# LOAD DATA FROM CSV
loaded_df = pd.read_csv(filename)

print("\n===== DATA LOADED FROM CSV =====")
print(loaded_df)

# DISPLAY SUMMARY
print("\n===== SUMMARY =====")
print("Player:", player_name)
print("Game:", game_name)
print("Total matches:", len(loaded_df))
print("Total kills:", loaded_df["Kills"].sum())
print("Average kills:", round(loaded_df["Kills"].mean(), 2))
print("Average K/D:", round(loaded_df["K/D"].mean(), 2))

print("\n========================================")
print("          DAY 20 COMPLETED")
print("========================================")
