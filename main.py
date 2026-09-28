print("================================")
print("   GAMING PERFORMANCE ANALYZER")
print("================================")

# -------------------------------
# PLAYER INFORMATION
# -------------------------------

player_name = input("Enter player name: ")
game_name = input("Enter game name: ")

# Number of matches
total_matches = int(input("How many matches do you want to enter? "))

# -------------------------------
# LISTS TO STORE MATCH DATA
# -------------------------------

kills_list = []
deaths_list = []
headshots_list = []
assists_list = []

# -------------------------------
# ENTER MATCH INFORMATION
# -------------------------------

for match in range(1, total_matches + 1):

    print("\n===== MATCH", match, "=====")

    kills = int(input("Enter kills: "))
    deaths = int(input("Enter deaths: "))
    headshots = int(input("Enter headshots: "))
    assists = int(input("Enter assists: "))

    # Store data in lists
    kills_list.append(kills)
    deaths_list.append(deaths)
    headshots_list.append(headshots)
    assists_list.append(assists)

# -------------------------------
# TOTAL STATISTICS
# -------------------------------

total_kills = sum(kills_list)
total_deaths = sum(deaths_list)
total_headshots = sum(headshots_list)
total_assists = sum(assists_list)

# -------------------------------
# AVERAGE STATISTICS
# -------------------------------

average_kills = total_kills / total_matches
average_deaths = total_deaths / total_matches
average_headshots = total_headshots / total_matches
average_assists = total_assists / total_matches

# -------------------------------
# HIGHEST AND LOWEST KILLS
# -------------------------------

highest_kills = max(kills_list)
lowest_kills = min(kills_list)

# Find the match numbers
best_match = kills_list.index(highest_kills) + 1
worst_match = kills_list.index(lowest_kills) + 1

# -------------------------------
# DISPLAY MATCH DATA
# -------------------------------

print("\n================================")
print("       MATCH DATA")
print("================================")

print("Kills:", kills_list)
print("Deaths:", deaths_list)
print("Headshots:", headshots_list)
print("Assists:", assists_list)

# -------------------------------
# DISPLAY TOTALS
# -------------------------------

print("\n================================")
print("       TOTAL STATISTICS")
print("================================")

print("Total Matches:", total_matches)
print("Total Kills:", total_kills)
print("Total Deaths:", total_deaths)
print("Total Headshots:", total_headshots)
print("Total Assists:", total_assists)

# -------------------------------
# DISPLAY AVERAGES
# -------------------------------

print("\n================================")
print("       AVERAGE STATISTICS")
print("================================")

print("Average Kills:", round(average_kills, 2))
print("Average Deaths:", round(average_deaths, 2))
print("Average Headshots:", round(average_headshots, 2))
print("Average Assists:", round(average_assists, 2))

# -------------------------------
# BEST AND WORST MATCH
# -------------------------------

print("\n================================")
print("       MATCH PERFORMANCE")
print("================================")

print("Highest Kills:", highest_kills)
print("Best Match: Match", best_match)

print("Lowest Kills:", lowest_kills)
print("Worst Match: Match", worst_match)

# -------------------------------
# DAY 7 COMPLETE
# -------------------------------

print("\n================================")
print("       DAY 7 COMPLETED")
print("================================")