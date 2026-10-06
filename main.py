import pandas as pd

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

match_numbers = [1, 2, 3, 4, 5]

kills = [12, 15, 8, 20, 10]
deaths = [6, 5, 4, 8, 5]
headshots = [5, 7, 3, 9, 4]
assists = [3, 4, 2, 5, 3]

# ----------------------------------------
# CREATE DATAFRAME
# ----------------------------------------

data = {
    "Match": match_numbers,
    "Kills": kills,
    "Deaths": deaths,
    "Headshots": headshots,
    "Assists": assists
}

df = pd.DataFrame(data)

# ----------------------------------------
# ADD K/D COLUMN
# ----------------------------------------

df["K/D"] = df["Kills"] / df["Deaths"]

# ----------------------------------------
# DISPLAY COMPLETE DATA
# ----------------------------------------

print("\n========================================")
print("          COMPLETE MATCH DATA")
print("========================================")

print(df.round(2))

# ----------------------------------------
# FILTER: HIGH KILL MATCHES
# ----------------------------------------

high_kill_matches = df[df["Kills"] >= 15]

print("\n========================================")
print("       MATCHES WITH 15+ KILLS")
print("========================================")

print(high_kill_matches.round(2))

# ----------------------------------------
# FILTER: LOW DEATH MATCHES
# ----------------------------------------

low_death_matches = df[df["Deaths"] <= 5]

print("\n========================================")
print("       MATCHES WITH 5 OR LESS DEATHS")
print("========================================")

print(low_death_matches.round(2))

# ----------------------------------------
# FILTER: HIGH K/D MATCHES
# ----------------------------------------

high_kd_matches = df[df["K/D"] >= 2.5]

print("\n========================================")
print("       MATCHES WITH 2.5+ K/D")
print("========================================")

print(high_kd_matches.round(2))

# ----------------------------------------
# SORT BY KILLS
# ----------------------------------------

sorted_by_kills = df.sort_values(by="Kills", ascending=False)

print("\n========================================")
print("       MATCHES SORTED BY KILLS")
print("========================================")

print(sorted_by_kills.round(2))

# ----------------------------------------
# SORT BY K/D
# ----------------------------------------

sorted_by_kd = df.sort_values(by="K/D", ascending=False)

print("\n========================================")
print("       MATCHES SORTED BY K/D")
print("========================================")

print(sorted_by_kd.round(2))

# ----------------------------------------
# BEST MATCH
# ----------------------------------------

best_match = df.loc[df["K/D"].idxmax()]

print("\n========================================")
print("             BEST MATCH")
print("========================================")

print(best_match.round(2))

# ----------------------------------------
# DAY 17 COMPLETE
# ----------------------------------------

print("\n========================================")
print("          DAY 17 COMPLETED")
print("========================================")