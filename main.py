print("================================")
print("   GAMING PERFORMANCE ANALYZER")
print("================================")

# Player information
player_name = input("Enter player name: ")
game_name = input("Enter game name: ")

# Number of matches
total_matches = int(input("How many matches do you want to enter? "))

# Variables to store totals
total_kills = 0
total_deaths = 0

# Enter match information
for match in range(1, total_matches + 1):

    print("\n===== MATCH", match, "=====")

    kills = int(input("Enter kills: "))
    deaths = int(input("Enter deaths: "))

    total_kills = total_kills + kills
    total_deaths = total_deaths + deaths

# Calculate average
average_kills = total_kills / total_matches

# Display result
print("\n================================")
print("       GAMING REPORT")
print("================================")

print("Player:", player_name)
print("Game:", game_name)
print("Total Matches:", total_matches)
print("Total Kills:", total_kills)
print("Total Deaths:", total_deaths)
print("Average Kills:", round(average_kills, 2))

print("\n===== DAY 6 COMPLETED =====")