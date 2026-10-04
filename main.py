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

average_kills = np.mean(kills_array)
average_kd = np.mean(kd_array)

highest_kills = np.max(kills_array)
lowest_kills = np.min(kills_array)

highest_kd = np.max(kd_array)
lowest_kd = np.min(kd_array)

# ----------------------------------------
# MATCHES ABOVE AVERAGE KILLS
# ----------------------------------------

above_average = kills_array > average_kills

above_average_count = np.sum(above_average)

# ----------------------------------------
# MATCHES BELOW AVERAGE KILLS
# ----------------------------------------

below_average = kills_array < average_kills

below_average_count = np.sum(below_average)

# ----------------------------------------
# MATCHES ABOVE AVERAGE K/D
# ----------------------------------------

above_average_kd = kd_array > average_kd

above_average_kd_count = np.sum(above_average_kd)

# ----------------------------------------
# BEST AND WORST MATCH
# ----------------------------------------

best_kills_match = np.argmax(kills_array) + 1
worst_kills_match = np.argmin(kills_array) + 1

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
# BASIC ANALYSIS
# ----------------------------------------

print("\n========================================")
print("          BASIC ANALYSIS")
print("========================================")

print("Average Kills:", round(average_kills, 2))
print("Average K/D:", round(average_kd, 2))

print("Highest Kills:", highest_kills)
print("Lowest Kills:", lowest_kills)

print("Highest K/D:", round(highest_kd, 2))
print("Lowest K/D:", round(lowest_kd, 2))

# ----------------------------------------
# PERFORMANCE COMPARISON
# ----------------------------------------

print("\n========================================")
print("       PERFORMANCE COMPARISON")
print("========================================")

print("Matches Above Average Kills:", above_average_count)
print("Matches Below Average Kills:", below_average_count)

print("Matches Above Average K/D:", above_average_kd_count)

# ----------------------------------------
# BEST AND WORST MATCHES
# ----------------------------------------

print("\n========================================")
print("        BEST AND WORST MATCHES")
print("========================================")

print("Best Kill Match: Match", best_kills_match)
print("Worst Kill Match: Match", worst_kills_match)

print("Best K/D Match: Match", best_kd_match)
print("Worst K/D Match: Match", worst_kd_match)

# ----------------------------------------
# DAY 14 COMPLETE
# ----------------------------------------

print("\n========================================")
print("          DAY 14 COMPLETED")
print("========================================")