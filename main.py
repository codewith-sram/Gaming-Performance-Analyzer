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
# BASIC STATISTICS
# ----------------------------------------

total_kills = np.sum(kills_array)
average_kills = np.mean(kills_array)
highest_kills = np.max(kills_array)
lowest_kills = np.min(kills_array)

# ----------------------------------------
# MEDIAN
# ----------------------------------------

median_kills = np.median(kills_array)

# ----------------------------------------
# STANDARD DEVIATION
# ----------------------------------------

kill_consistency = np.std(kills_array)

# ----------------------------------------
# K/D STATISTICS
# ----------------------------------------

average_kd = np.mean(kd_array)
median_kd = np.median(kd_array)
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
# KILL STATISTICS
# ----------------------------------------

print("\n========================================")
print("          KILL STATISTICS")
print("========================================")

print("Total Kills:", total_kills)
print("Average Kills:", round(average_kills, 2))
print("Median Kills:", round(median_kills, 2))
print("Highest Kills:", highest_kills)
print("Lowest Kills:", lowest_kills)

# ----------------------------------------
# CONSISTENCY
# ----------------------------------------

print("\n========================================")
print("        PERFORMANCE CONSISTENCY")
print("========================================")

print("Kill Standard Deviation:", round(kill_consistency, 2))

# ----------------------------------------
# K/D STATISTICS
# ----------------------------------------

print("\n========================================")
print("             K/D ANALYSIS")
print("========================================")

print("Average K/D:", round(average_kd, 2))
print("Median K/D:", round(median_kd, 2))
print("Highest K/D:", round(highest_kd, 2))
print("Lowest K/D:", round(lowest_kd, 2))

print("Best K/D Match: Match", best_kd_match)
print("Worst K/D Match: Match", worst_kd_match)

# ----------------------------------------
# DAY 13 COMPLETE
# ----------------------------------------

print("\n========================================")
print("          DAY 13 COMPLETED")
print("========================================")