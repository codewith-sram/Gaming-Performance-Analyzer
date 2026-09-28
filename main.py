print("================================")
print("   GAMING PERFORMANCE ANALYZER")
print("================================")

# Player information
player_name = input("Enter player name: ")
game_name = input("Enter game name: ")

# Number of matches
total_matches = int(input("How many matches do you want to enter? "))

# Lists to store match data
kills_list = []
deaths_list = []
headshots_list = []

# Enter match information
for match in range(1, total_matches + 1):

    print("\n===== MATCH", match, "=====")

    kills = int(input("Enter kills: "))
    deaths = int(input("Enter deaths: "))
    headshots = int(input("Enter headshots: "))

    # Add data to lists
    kills_list.append(kills)
    deaths_list.append(deaths)
    headshots_list.append(headshots)

# Calculate totals
total_kills = sum(kills_list)
total_deaths = sum(deaths_list)
total_headshots = sum(headshots_list)

# Calculate average
average_kills = total_kills / total_matches

# Display report
print("\n================================")
print("       GAMING REPORT")
print("================================")

print("Player:", player_name)
print("Game:", game_name)

print("\nKills:", kills_list)
print("Deaths:", deaths_list)
print("Headshots:", headshots_list)

print("\nTotal Matches:", total_matches)
print("Total Kills:", total_kills)
print("Total Deaths:", total_deaths)
print("Total Headshots:", total_headshots)
print("Average Kills:", round(average_kills, 2))

print("\n===== DAY 7 COMPLETED =====")