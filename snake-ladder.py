
# Snake-Ladder game 

import random

print("\nLet's get started...\n")

player_positions = [0]
total_players = int(input("Enter number of players: "))
player_positions *= total_players
curr_player = 1
player_index = 0
round = 1

def check_obstacles(obs_start, obs_end):
    for i in obs_start:
        if player_positions[player_index] == i:
            obs_index = obs_start.index(i)
            
            player_positions[player_index] = obs_end[obs_index]
            if obs_start == ladders_start:
                print("\n----- Yayyy! you got the ladder -----")
                print("You climbed directly to -", obs_end[obs_index], end="\n\n")
            else:
                print("\n----- Oopsss! you got biten by snake -----")
                print("You fell directly to -", obs_end[obs_index], end="\n\n")

ladders_start = [1, 4, 8, 21, 28, 50, 71, 80]
ladders_end = [38, 14, 10, 42, 76, 67, 92, 99]

snakes_start = [32, 36, 48, 62, 88, 95, 97]
snake_end = [10, 6, 26, 18, 24, 56, 78]


while True:
    # Rolling the dice 
    print("Player", curr_player, "- Press ENTER to roll the dice", end="")
    input()
    rolled = random.randint(1, 6)
    print("Player", curr_player, "rolled:", rolled)
    player_positions[player_index] += rolled

    # Check if any obstacles
    check_obstacles(ladders_start, ladders_end)
    check_obstacles(snakes_start, snake_end)

    # check player is not > 100
    if player_positions[player_index] > 100:
        player_positions[player_index] -= rolled


    # If player score is 100, then player wins
    if player_positions[player_index] == 100:
        print("Players positions: ", player_positions)
        print("\n<---------- Player", curr_player, "Wins ---------->\n")
        break

    player_index += 1
    curr_player += 1

    # If all players rolled the dice ---> next round 
    if curr_player > total_players:
        print("After round ", round, ", All players positions are: ", player_positions, sep="")
        round += 1
        curr_player = 1
        player_index = 0
        print()
        
