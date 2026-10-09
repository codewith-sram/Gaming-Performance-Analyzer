
import pandas as pd

print("========================================")
print("       GAMING PERFORMANCE ANALYZER")
print("========================================")

# PLAYER INFORMATION
player_name = input("Enter player name: ")
game_name = input("Enter game name: ")

# GAMING DATA WITH MISSING VALUES
data = {
    "Match": [1, 2, 3, 4, 4, 5],
    "Kills": [12, 15, None, 20, 20, 10],
    "Deaths": [6, 5, 4, None, None, 5],
    "Headshots": [5, 7, 3, 9, 9, 4],
    "Assists": [3, 4, 2, 5, 5, 3]
}

# CREATE DATAFRAME
df = pd.DataFrame(data)

print("\n===== PLAYER INFORMATION =====")
print("Player:", player_name)
print("Game:", game_name)

# DISPLAY ORIGINAL DATA
print("\n===== ORIGINAL DATA =====")
print(df)

# CHECK MISSING VALUES
print("\n===== MISSING VALUES =====")
print(df.isnull().sum())

# FILL MISSING KILLS WITH MEDIAN
df["Kills"] = df["Kills"].fillna(df["Kills"].median())

# FILL MISSING DEATHS WITH MEDIAN
df["Deaths"] = df["Deaths"].fillna(df["Deaths"].median())

print("\n===== DATA AFTER FILLING MISSING VALUES =====")
print(df)

# CHECK DUPLICATE ROWS
print("\n===== DUPLICATE ROWS =====")
print(df.duplicated())

# REMOVE EXACT DUPLICATE ROWS
df = df.drop_duplicates()

# RESET THE INDEX
df = df.reset_index(drop=True)

# RENUMBER MATCHES AFTER CLEANING
df["Match"] = range(1, len(df) + 1)

# CALCULATE K/D SAFELY
df["K/D"] = (
    df["Kills"] /
    df["Deaths"].replace(0, float("nan"))
).fillna(0)

# DISPLAY CLEAN DATA
print("\n===== CLEAN GAMING DATA =====")
print(df.round(2))

# CLEANING SUMMARY
print("\n===== CLEANING SUMMARY =====")
print("Remaining matches:", len(df))
print("Missing values remaining:", int(df.isnull().sum().sum()))
print("Duplicate rows remaining:", int(df.duplicated().sum()))

print("\n========================================")
print("          DAY 19 COMPLETED")
print("========================================")
