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
# CREATE DATAFRAME
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
# ADD K/D
# ----------------------------------------

df["K/D"] = df["Kills"] / df["Deaths"]

# ----------------------------------------
# ADD PERFORMANCE CATEGORY
# ----------------------------------------

df["Performance"] = df["K/D"].apply(
    lambda kd:
    "Excellent" if kd >= 3
    else "Very Good" if kd >= 2
    else "Good" if kd >= 1.5
    else "Needs Improvement"
)

# ----------------------------------------
# DISPLAY COMPLETE DATA
# ----------------------------------------

print("\n========================================")
print("          COMPLETE MATCH DATA")
print("========================================")

print(df.round(2))

# ----------------------------------------
# TOTAL STATISTICS
# ----------------------------------------

print("\n========================================")
print("          TOTAL STATISTICS")
print("========================================")

print("Total Kills:", df["Kills"].sum())
print("Total Deaths:", df["Deaths"].sum())
print("Total Headshots:", df["Headshots"].sum())
print("Total Assists:", df["Assists"].sum())

# ----------------------------------------
# AVERAGE STATISTICS
# ----------------------------------------

print("\n========================================")
print("         AVERAGE STATISTICS")
print("========================================")

print("Average Kills:", round(df["Kills"].mean(), 2))
print("Average Deaths:", round(df["Deaths"].mean(), 2))
print("Average Headshots:", round(df["Headshots"].mean(), 2))
print("Average Assists:", round(df["Assists"].mean(), 2))
print("Average K/D:", round(df["K/D"].mean(), 2))

# ----------------------------------------
# MAXIMUM STATISTICS
# ----------------------------------------

print("\n========================================")
print("        HIGHEST PERFORMANCE")
print("========================================")

print("Highest Kills:", df["Kills"].max())
print("Highest K/D:", round(df["K/D"].max(), 2))
print("Highest Headshots:", df["Headshots"].max())
print("Highest Assists:", df["Assists"].max())

# ----------------------------------------
# MINIMUM STATISTICS
# ----------------------------------------

print("\n========================================")
print("        LOWEST PERFORMANCE")
print("========================================")

print("Lowest Kills:", df["Kills"].min())
print("Lowest K/D:", round(df["K/D"].min(), 2))
print("Lowest Headshots:", df["Headshots"].min())
print("Lowest Assists:", df["Assists"].min())

# ----------------------------------------
# PERFORMANCE SUMMARY
# ----------------------------------------

print("\n========================================")
print("       PERFORMANCE SUMMARY")
print("========================================")

performance_count = df["Performance"].value_counts()

print(performance_count)

# ----------------------------------------
# BEST MATCH
# ----------------------------------------

best_match_index = df["K/D"].idxmax()
best_match = df.loc[best_match_index]

print("\n========================================")
print("             BEST MATCH")
print("========================================")

print(best_match.round(2))

# ----------------------------------------
# DAY 18 COMPLETE
# ----------------------------------------

print("\n========================================")
print("          DAY 18 COMPLETED")
print("========================================")