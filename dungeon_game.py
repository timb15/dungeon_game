import os
import random

# Dungeon grid
GRID = [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0),
        (0, 1), (1, 1), (2, 1), (3, 1), (4, 1),
        (0, 2), (1, 2), (2, 2), (3, 2), (4, 2),
        (0, 3), (1, 3), (2, 3), (3, 3), (4, 3),
        (0, 4), (1, 4), (2, 4), (3, 4), (4, 4), ]

# displays the dungeon grid with player location or monster location if found


def draw_grid(player, monster=None):
    icon = "P"
    # sets the icon to the 'monster' icon if the player lands on the monster
    if monster:
        icon = "M"

    map = ""
    print(" _" * 5)

    for space in GRID:
        x, y = space
        if x < 4:
            if player == space:
                map += "|{}".format(icon)
            else:
                map += "|_"
        else:
            if player == space:
                map += "|{}|\n".format(icon)
            else:
                map += "|_|\n"
    print(map)

# generates a random location for the monster, door and player


def generate_locations():
    return random.sample(GRID, 3)

# moves changes player location in selected direction


def move_player(player, move):
    x, y = player
    if move == "LEFT":
        x -= 1
    if move == "RIGHT":
        x += 1
    if move == "UP":
        y -= 1
    if move == "DOWN":
        y += 1
    return x, y

# Gets available player moves depending on player position


def get_moves(player):
    x, y = player
    moves = ["LEFT", "RIGHT", "UP", "DOWN"]
    if x == 0:
        moves.remove("LEFT")
    if x == 4:
        moves.remove("RIGHT")
    if y == 0:
        moves.remove("UP")
    if y == 4:
        moves.remove("DOWN")
    return moves


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def game_loop():
    playing = True
    player, monster, door = generate_locations()

    while playing:
        clear_screen()
        print("Welcome to the dungeon!")
        draw_grid(player)
        print("You are currently in room {}".format(player))
        print("You can move {}".format(", ".join(get_moves(player))))
        print("Enter QUIT to quit")

        moves = get_moves(player)
        move = input(">  ").upper()

        if move == 'QUIT':
            clear_screen()
            print("**See you next time!**")
            break
        if move in moves:
            player = move_player(player, move)
            if player == door:
                clear_screen()
                print("**You found the exit! You Win!!**")
                playing = False
            if player == monster:
                clear_screen()
                draw_grid(player, monster)
                print("**You found the monster! You Lose!!**")
                playing = False
        else:
            input("Invalid move... press return to try again")
    else:
        play_again = input("Do you want to play again? (y/n)").lower()
        if play_again != "n":
            game_loop()


game_loop()
