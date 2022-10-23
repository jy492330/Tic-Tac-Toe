"""
Nucamp
Porfolio Project: Tic-Tac-Toe
Creator: Jin Jessica Yang
"""
import random
import time
import pygame
from pygame import mixer


board = [" ", " ", " ",
         " ", " ", " ",
         " ", " ", " "]

game_still_going = True
winner = None
players = ("X", "O")
current_player = random.choice(players)


def display_board():
    print("\n")
    print(board[0] + " | " + board[1] + " | " + board[2] + "\t" + "\t" + "1 | 2 | 3")
    print('---------       ---------')
    print(board[3] + " | " + board[4] + " | " + board[5] + "\t" + "\t" + "4 | 5 | 6")
    print('---------       ---------')
    print(board[6] + " | " + board[7] + " | " + board[8] + "\t" + "\t" + "7 | 8 | 9")
    print("\n")


def play_game():
    display_board()
    pygame.mixer.init()
    start_sound = mixer.Sound('start.wav')
    start_sound.play()
    while game_still_going:
        handle_turn(current_player)
        flip_player()
        check_if_game_over()

    if winner == "X" or winner == "O":
        winner_sound = mixer.Sound('winner.wav')
        winner_sound.play()
        time.sleep(3)
        print(f"Player {winner} won !")

    elif winner is None:
        tie_sound = mixer.Sound('draw.wav')
        tie_sound.play()
        time.sleep(3)
        print("Draw !")


def handle_turn(player):
    print(f"{player}'s turn.")
    position = int(input("Choose a position from the board: "))
    while invalid_input(position):
        position = int(input("Invalid input. Choose a position from the board: "))

    position = position - 1
    board[position] = player
    pop_sound = mixer.Sound('pop.wav')
    pop_sound.play()
    display_board()


def invalid_input(player_input):
    if player_input not in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
        pygame.mixer.init()
        pygame.mixer.Sound.play(pygame.mixer.Sound("winner.wav"))
        return True
    if board[player_input - 1] != " ":
        pygame.mixer.init()
        pygame.mixer.Sound.play(pygame.mixer.Sound("winner.wav"))
        print("This position is already taken.")
        return True
    return False


def flip_player():
    global current_player
    if current_player == "X":
        current_player = "O"
    elif current_player == "O":
        current_player = "X"
        return


def check_if_game_over():
    check_rows()
    check_columns()
    check_diagonals()
    check_if_tie()


def check_rows():
    global winner
    global game_still_going
    row_1 = board[0] == board[1] == board[2] != " "
    row_2 = board[3] == board[4] == board[5] != " "
    row_3 = board[6] == board[7] == board[8] != " "
    if row_1 or row_2 or row_3:
        game_still_going = False

    if row_1:
        winner = board[0]
        return winner
    elif row_2:
        winner = board[3]
        return winner
    elif row_3:
        winner = board[6]
        return winner
    else:
        return None


def check_columns():
    global winner
    global game_still_going
    col_1 = board[0] == board[3] == board[6] != " "
    col_2 = board[1] == board[4] == board[7] != " "
    col_3 = board[2] == board[5] == board[8] != " "
    if col_1 or col_2 or col_3:
        game_still_going = False

    if col_1:
        winner = board[0]
        return winner
    elif col_2:
        winner = board[1]
        return winner
    elif col_3:
        winner = board[2]
        return winner
    else:
        return None


def check_diagonals():
    global winner
    global game_still_going
    diagonal_1 = board[0] == board[4] == board[8] != " "
    diagonal_2 = board[2] == board[4] == board[6] != " "
    if diagonal_1 or diagonal_2:
        game_still_going = False

    if diagonal_1:
        winner = board[0]
        return winner
    elif diagonal_2:
        winner = board[2]
        return winner
    else:
        return None


def check_if_tie():
    global game_still_going
    if " " not in board:
        game_still_going = False
        return True
    return False


if __name__ == "__main__":
    play_game()
