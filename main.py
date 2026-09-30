print("========================================")
print("       GAMING PERFORMANCE ANALYZER")
print("========================================")


# ----------------------------------------
# FUNCTION: CALCULATE K/D
# ----------------------------------------

def calculate_kd(kills, deaths):

    if deaths == 0:
        return kills

    return kills / deaths


# ----------------------------------------
# FUNCTION: CALCULATE AVERAGE
# ----------------------------------------

def calculate_average(values):

    return sum(values) / len(values)


# ----------------------------------------
# FUNCTION: PERFORMANCE RATING
# ----------------------------------------

def get_rating(kd):

    if kd >= 3:
        return "Excellent"
    elif kd >= 2:
        return "Very Good"
    elif kd >= 1.5:
        return "Good"
    elif kd >= 1:
        return "Average"
    else:
        return "Needs Improvement"


# ----------------------------------------
# PLAYER INFORMATION
# ----------------------------------------

player_name = input("Enter player name: ")
game_name = input("Enter game name: ")

total_matches = int(input("How many matches do you want to enter? "))


# ----------------------------------------
# LISTS
# ----------------------------------------

kills_list = []
deaths_list = []
headshots_list = []
assists_list = []
kd_list = []


# ----------------------------------------
# ENTER MATCH DATA
# ----------------------------------------

for match in range(1, total_matches + 1):

    print("\n===== MATCH", match, "=====")

    kills = int(input("Enter kills: "))
    deaths = int(input("Enter deaths: "))
    headshots = int(input("Enter headshots: "))
    assists = int(input("Enter assists: "))

    # Store data
    kills_list.append(kills)
    deaths_list.append(deaths)
    headshots_list.append(headshots)
    assists_list.append(assists)

    # Calculate match K/D
    kd = calculate_kd(kills, deaths)

    kd_list.append(kd)


# ----------------------------------------
# TOTAL STATISTICS
# ----------------------------------------

total_kills = sum(kills_list)
total_deaths = sum(deaths_list)
total_headshots = sum(headshots_list)
total_assists = sum(assists_list)


# ----------------------------------------
# AVERAGE STATISTICS
# ----------------------------------------

average_kills = calculate_average(kills_list)
average_deaths = calculate_average(deaths_list)
average_headshots = calculate_average(headshots_list)
average_assists = calculate_average(assists_list)


# ----------------------------------------
# OVERALL K/D
# ----------------------------------------

overall_kd = calculate_kd(total_kills, total_deaths)


# ----------------------------------------
# BEST AND WORST MATCH
# ----------------------------------------

highest_kills = max(kills_list)
lowest_kills = min(kills_list)

best_match = kills_list.index(highest_kills) + 1
worst_match = kills_list.index(lowest_kills) + 1


# ----------------------------------------
# BEST K/D MATCH
# ----------------------------------------

highest_kd = max(kd_list)

best_kd_match = kd_list.index(highest_kd) + 1


# ----------------------------------------
# PERFORMANCE RATING
# ----------------------------------------

rating = get_rating(overall_kd)


# ----------------------------------------
# FINAL PERFORMANCE REPORT
# ----------------------------------------

print("\n========================================")
print("          PERFORMANCE REPORT")
print("========================================")

print("Player Name:", player_name)
print("Game:", game_name)
print("Total Matches:", total_matches)


print("\n---------- TOTAL STATISTICS ----------")

print("Total Kills:", total_kills)
print("Total Deaths:", total_deaths)
print("Total Headshots:", total_headshots)
print("Total Assists:", total_assists)


print("\n---------- AVERAGE STATISTICS ----------")

print("Average Kills:", round(average_kills, 2))
print("Average Deaths:", round(average_deaths, 2))
print("Average Headshots:", round(average_headshots, 2))
print("Average Assists:", round(average_assists, 2))


print("\n---------- K/D ANALYSIS ----------")

print("Overall K/D:", round(overall_kd, 2))
print("Highest Match K/D:", round(highest_kd, 2))
print("Best K/D Match: Match", best_kd_match)


print("\n---------- MATCH ANALYSIS ----------")

print("Highest Kills:", highest_kills)
print("Best Kill Match: Match", best_match)

print("Lowest Kills:", lowest_kills)
print("Worst Kill Match: Match", worst_match)


print("\n---------- PERFORMANCE RATING ----------")

print("Overall Rating:", rating)


print("\n========================================")
print("          DAY 10 COMPLETED")
print("========================================")