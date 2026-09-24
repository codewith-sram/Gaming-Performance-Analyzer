print("================================")
print("   GAMING PERFORMANCE ANALYZER")
print("================================")

# Player information
player_name = input("Enter player name: ")
game_name = input("Enter game name: ")

# Gaming statistics
matches = int(input("Enter total matches: "))
kills = int(input("Enter total kills: "))
deaths = int(input("Enter total deaths: "))
wins = int(input("Enter total wins: "))
losses = int(input("Enter total losses: "))
headshots = int(input("Enter total headshots: "))

# Display player information
print("\n===== PLAYER INFORMATION =====")
print("Player Name:", player_name)
print("Game:", game_name)

# Display gaming statistics
print("\n===== GAMING STATISTICS =====")
print("Matches:", matches)
print("Kills:", kills)
print("Deaths:", deaths)
print("Wins:", wins)
print("Losses:", losses)
print("Headshots:", headshots)
