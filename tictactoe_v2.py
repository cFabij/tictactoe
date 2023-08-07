#!/usr/bin/python3

import subprocess
from random import randint

gameboard_template = ["", " ", "|", " ", "|", " "]
gameboard_lines = ["  ", "--", "--", "--", "--"]
coordinates_top = ["  ", " 1 ", "", "2 ", "", "3 "]
coordinates = ["A1", "A2", "A3", "B1", "B2", "B3", "C1", "C2", "C3"]

gameboard_upper = gameboard_template[:]
gameboard_upper[0] = " A "

gameboard_middle = gameboard_template[:]
gameboard_middle[0] = " B "

gameboard_lower = gameboard_template[:]
gameboard_lower[0] = " C "

player_flag = "X"
PLAYER_ONE = "X"
PLAYER_TWO = "O"
game_undecided = True
used_fields = []
turns = 0

subprocess.call("cls", shell=True)

print(*coordinates_top)
print(*gameboard_upper)
print(*gameboard_lines)
print(*gameboard_middle)
print(*gameboard_lines)
print(*gameboard_lower)

def print_gameboard(move):
    row = move[0]
    column = int(move[1])
    adjustor = 0

    for i in range(1, 4):
        if column == i:
            if row == "A":
                if player_flag == PLAYER_ONE:
                    gameboard_upper[i+adjustor] = PLAYER_ONE
                else:
                    gameboard_upper[i+adjustor] = PLAYER_TWO
            if row == "B":
                if player_flag == PLAYER_ONE:
                    gameboard_middle[i+adjustor] = PLAYER_ONE
                else:
                    gameboard_middle[i+adjustor] = PLAYER_TWO
            if row == "C":
                if player_flag == PLAYER_ONE:
                    gameboard_lower[i+adjustor] = PLAYER_ONE
                else:
                    gameboard_lower[i+adjustor] = PLAYER_TWO

        adjustor += 1

    print(*coordinates_top)
    print(*gameboard_upper)
    print(*gameboard_lines)
    print(*gameboard_middle)
    print(*gameboard_lines)
    print(*gameboard_lower)


def random_move():
    possible_moves = [element for element in coordinates if element not in used_fields]

    random_coordinate_index = randint(0, (len(possible_moves) - 1))

    return possible_moves[random_coordinate_index]


def game_end():

    #Checks for horizontal matches
    for player in [PLAYER_ONE, PLAYER_TWO]:
        if gameboard_upper[1] == player and gameboard_upper[3] == player and gameboard_upper[5] == player:
            print(f"{player} hat gewonnen!")
            return False
        
        if gameboard_middle[1] == player and gameboard_middle[3] == player and gameboard_middle[5] == player:
            print(f"{player} hat gewonnen!")
            return False

        if gameboard_lower[1] == player and gameboard_lower[3] == player and gameboard_lower[5] == player:
            print(f"{player} hat gewonnen!")
            return False

    #Checks for vertical matches
    for i in [1, 3, 5]:
        for player in [PLAYER_ONE, PLAYER_TWO]:
            if gameboard_upper[i] == player and gameboard_middle[i] == player and gameboard_lower[i] == player:
                print(f"{player} hat gewonnen!")
                return False

    #Checks for diagonal matches
    for player in [PLAYER_ONE, PLAYER_TWO]:
        if gameboard_upper[1] == player and gameboard_middle[3] == player and gameboard_lower[5] == player:
            print(f"{player} hat gewonnen!")
            return False
        
        if gameboard_upper[5] == player and gameboard_middle[3] == player and gameboard_lower[1] == player:
            print(f"{player} hat gewonnen!")
            return False
    
    return True

user_input = input("Wenn du gegen einen Bot spielen willst, der zufällige Züge macht, gib 'BOT' ein. Andernfalls sind beide Spieler:innen einzugeben. ")

if user_input == "BOT":
    BOT = True
else:
    BOT = False

while game_undecided:
    if turns == 9:
        print("Unentschieden!")
        break
   
    if BOT and player_flag == PLAYER_TWO:
        move_input = random_move()
    else:
        while True:
            move_input = input(f"{player_flag}: Gib deine Koordinate ein (Format zB 'A1'): ").strip().upper()

            if move_input not in coordinates:
                print("Koordinaten nicht gefunden. Bitte korrigiert eingeben.")
            elif move_input in used_fields:
                print("Koordinate bereits belegt. Bitte korrigiert eingeben.")
            else:
                break

    subprocess.call("cls", shell=True)

    print_gameboard(move_input)
    used_fields.append(move_input)
    
    if player_flag == PLAYER_ONE:
        player_flag = PLAYER_TWO
    else:
        player_flag = PLAYER_ONE

    turns += 1
    
    game_undecided = game_end()
