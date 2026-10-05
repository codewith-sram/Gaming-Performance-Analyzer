import pandas as pd

print("========================================")
print("       GAMING PERFORMANCE ANALYZER")
print("========================================")

# ----------------------------------------
# PLAYER INFORMATION
# ----------------------------------------

player_name = input("Enter player name: ")
game_name = input("Enter game name: ")

# ----------------------------------------
# MATCH DATA
# ----------------------------------------

match_numbers = [1, 2, 3, 4, 5]

kills = [12, 15, 8, 20, 10]
deaths = [6, 5, 4, 8, 5]
headshots = [5, 7, 3, 9, 4]
assists = [3, 4, 2, 5, 3]

# ----------------------------------------
# CREATE PANDAS DATAFRAME
# ----------------------------------------

data = {
    "Match": match_numbers,
    "Kills": kills,
    "Deaths": deaths,
    "Headshots": headshots,
    "Assists": assists
}

df = pd.DataFrame(data)

# ----------------------------------------
# CALCULATE K/D
# ----------------------------------------

df["K/D"] = df["Kills"] / df["Deaths"]

# ----------------------------------------
# DISPLAY PLAYER INFORMATION
# ----------------------------------------

print("\n========================================")
print("          PLAYER INFORMATION")
print("========================================")

print("Player Name:", player_name)
print("Game:", game_name)

# ----------------------------------------
# DISPLAY DATAFRAME
# ----------------------------------------

print("\n========================================")
print("          MATCH DATA")
print("========================================")

print(df)

# ----------------------------------------
# DISPLAY COLUMNS
# ----------------------------------------

print("\n========================================")
print("          KILLS DATA")
print("========================================")

print(df["Kills"])

print("\n========================================")
print("          K/D DATA")
print("========================================")

print(df["K/D"].round(2))

# ----------------------------------------
# DAY 15 COMPLETE
# ----------------------------------------

print("\n========================================")
print("          DAY 15 COMPLETED")
print("========================================")