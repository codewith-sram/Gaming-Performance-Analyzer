import numpy as np

print("================================")
print("   GAMING PERFORMANCE ANALYZER")
print("================================")

# -------------------------------
# PLAYER INFORMATION
# -------------------------------

player_name = input("Enter player name: ")
game_name = input("Enter game name: ")

# -------------------------------
# MATCH DATA
# -------------------------------

kills = [12, 15, 8, 20, 10]
deaths = [6, 5, 4, 8, 5]
headshots = [5, 7, 3, 9, 4]
assists = [3, 4, 2, 5, 3]

# -------------------------------
# CONVERT LISTS TO NUMPY ARRAYS
# -------------------------------

kills_array = np.array(kills)
deaths_array = np.array(deaths)
headshots_array = np.array(headshots)
assists_array = np.array(assists)

# -------------------------------
# DISPLAY ARRAYS
# -------------------------------

print("\n================================")
print("       MATCH STATISTICS")
print("================================")

print("Kills:", kills_array)
print("Deaths:", deaths_array)
print("Headshots:", headshots_array)
print("Assists:", assists_array)

# -------------------------------
# TOTAL STATISTICS
# -------------------------------

print("\n================================")
print("       TOTAL STATISTICS")
print("================================")

print("Total Kills:", np.sum(kills_array))
print("Total Deaths:", np.sum(deaths_array))
print("Total Headshots:", np.sum(headshots_array))
print("Total Assists:", np.sum(assists_array))

# -------------------------------
# AVERAGE STATISTICS
# -------------------------------

print("\n================================")
print("       AVERAGE STATISTICS")
print("================================")

print("Average Kills:", np.mean(kills_array))
print("Average Deaths:", np.mean(deaths_array))
print("Average Headshots:", np.mean(headshots_array))
print("Average Assists:", np.mean(assists_array))

# -------------------------------
# HIGHEST AND LOWEST KILLS
# -------------------------------

print("\n================================")
print("       KILL ANALYSIS")
print("================================")

print("Highest Kills:", np.max(kills_array))
print("Lowest Kills:", np.min(kills_array))

# -------------------------------
# DAY 11 COMPLETE
# -------------------------------

print("\n================================")
print("       DAY 11 COMPLETED")
print("================================")