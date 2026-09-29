print("================================")
print("   GAMING PERFORMANCE ANALYZER")
print("================================")


# -------------------------------
# FUNCTION: CALCULATE K/D
# -------------------------------

def calculate_kd(kills, deaths):

    if deaths == 0:
        return kills
    else:
        return kills / deaths


# -------------------------------
# FUNCTION: CALCULATE AVERAGE
# -------------------------------

def calculate_average(values):

    return sum(values) / len(values)


# -------------------------------
# FUNCTION: FIND HIGHEST VALUE
# -------------------------------

def find_highest(values):

    return max(values)


# -------------------------------
# FUNCTION: FIND LOWEST VALUE
# -------------------------------

def find_lowest(values):

    return min(values)


# -------------------------------
# PLAYER INFORMATION
# -------------------------------

player_name = input("Enter player name: ")
game_name = input("Enter game name: ")

total_matches = int(input("How many matches do you want to enter? "))


# -------------------------------
# LISTS
# -------------------------------

kills_list = []
deaths_list = []
headshots_list = []
assists_list = []
kd_list = []


# -------------------------------
# ENTER MATCH DATA
# -------------------------------

for match in range(1, total_matches + 1):

    print("\n===== MATCH", match, "=====")

    kills = int(input("Enter kills: "))
    deaths = int(input("Enter deaths: "))
    headshots = int(input("Enter headshots: "))
    assists = int(input("Enter assists: "))

    kills_list.append(kills)
    deaths_list.append(deaths)
    headshots_list.append(headshots)
    assists_list.append(assists)

    # Use the K/D function
    kd = calculate_kd(kills, deaths)

    kd_list.append(kd)


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

average_kills = calculate_average(kills_list)
average_deaths = calculate_average(deaths_list)
average_headshots = calculate_average(headshots_list)
average_assists = calculate_average(assists_list)


# -------------------------------
# HIGHEST AND LOWEST KILLS
# -------------------------------

highest_kills = find_highest(kills_list)
lowest_kills = find_lowest(kills_list)

best_match = kills_list.index(highest_kills) + 1
worst_match = kills_list.index(lowest_kills) + 1


# -------------------------------
# BEST K/D
# -------------------------------

highest_kd = find_highest(kd_list)

best_kd_match = kd_list.index(highest_kd) + 1


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

print("K/D Ratio:", [round(kd, 2) for kd in kd_list])


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
# MATCH PERFORMANCE
# -------------------------------

print("\n================================")
print("       MATCH PERFORMANCE")
print("================================")

print("Highest Kills:", highest_kills)
print("Best Match: Match", best_match)

print("Lowest Kills:", lowest_kills)
print("Worst Match: Match", worst_match)

print("Highest K/D:", round(highest_kd, 2))
print("Best K/D Match: Match", best_kd_match)


# -------------------------------
# DAY 9 COMPLETE
# -------------------------------

print("\n================================")
print("       DAY 9 COMPLETED")
print("================================")