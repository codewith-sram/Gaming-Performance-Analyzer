import numpy as np

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

kills = [12, 15, 8, 20, 10]
deaths = [6, 5, 4, 8, 5]
headshots = [5, 7, 3, 9, 4]
assists = [3, 4, 2, 5, 3]

# ----------------------------------------
# CONVERT TO NUMPY ARRAYS
# ----------------------------------------

kills_array = np.array(kills)
deaths_array = np.array(deaths)
headshots_array = np.array(headshots)
assists_array = np.array(assists)

# ----------------------------------------
# K/D CALCULATION
# ----------------------------------------

kd_array = kills_array / deaths_array

# ----------------------------------------
# TOTAL STATISTICS
# ----------------------------------------

total_kills = np.sum(kills_array)
total_deaths = np.sum(deaths_array)
total_headshots = np.sum(headshots_array)
total_assists = np.sum(assists_array)

# ----------------------------------------
# AVERAGE STATISTICS
# ----------------------------------------

average_kills = np.mean(kills_array)
average_deaths = np.mean(deaths_array)
average_headshots = np.mean(headshots_array)
average_assists = np.mean(assists_array)

# ----------------------------------------
# K/D STATISTICS
# ----------------------------------------

average_kd = np.mean(kd_array)
highest_kd = np.max(kd_array)
lowest_kd = np.min(kd_array)

best_kd_match = np.argmax(kd_array) + 1
worst_kd_match = np.argmin(kd_array) + 1

# ----------------------------------------
# DISPLAY MATCH DATA
# ----------------------------------------

print("\n========================================")
print("          MATCH STATISTICS")
print("========================================")

print("Kills:", kills_array)
print("Deaths:", deaths_array)
print("Headshots:", headshots_array)
print("Assists:", assists_array)

print("K/D Ratio:", np.round(kd_array, 2))

# ----------------------------------------
# DISPLAY TOTALS
# ----------------------------------------

print("\n========================================")
print("          TOTAL STATISTICS")
print("========================================")

print("Total Kills:", total_kills)
print("Total Deaths:", total_deaths)
print("Total Headshots:", total_headshots)
print("Total Assists:", total_assists)

# ----------------------------------------
# DISPLAY AVERAGES
# ----------------------------------------

print("\n========================================")
print("          AVERAGE STATISTICS")
print("========================================")

print("Average Kills:", round(average_kills, 2))
print("Average Deaths:", round(average_deaths, 2))
print("Average Headshots:", round(average_headshots, 2))
print("Average Assists:", round(average_assists, 2))

# ----------------------------------------
# K/D ANALYSIS
# ----------------------------------------

print("\n========================================")
print("             K/D ANALYSIS")
print("========================================")

print("Average K/D:", round(average_kd, 2))
print("Highest K/D:", round(highest_kd, 2))
print("Lowest K/D:", round(lowest_kd, 2))

print("Best K/D Match: Match", best_kd_match)
print("Worst K/D Match: Match", worst_kd_match)

# ----------------------------------------
# DAY 12 COMPLETE
# ----------------------------------------

print("\n========================================")
print("          DAY 12 COMPLETED")
print("========================================")