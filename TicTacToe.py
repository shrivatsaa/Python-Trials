import numpy as np
import random
import time
import os

Pattern = {'1':'$','2':'$','3':'$','4':'$','5':'$','6':'$','7':'$','8':'$','9':'$'}
DefaultPattern = {'1':'$','2':'$','3':'$','4':'$','5':'$','6':'$','7':'$','8':'$','9':'$'}
cls = lambda: os.system('clear')

def display_board(Pattern):
    print ("\n")
    for idx in range (1,len(Pattern)+1):
        index = str(idx)
        print (Pattern[index] +' |', end=" " if idx not in [3,6] else "\n" + '__  __  __' + "\n\n")

    print("\n")

def player_input(Player):
    choice = 'None'
    while choice not in ['X','O']:
        print ("\n")
        choice = input("{} , Pick one of the two markers and enter the same - X(pronounced ex) or O(pronounced oh) :".format(Player))
        if choice.upper() not in ['X','O']:
            print("\n Sorry, Invalid choice")
            
    Player1Marker = choice.upper()
    Player2Marker = str('O' if Player1Marker == 'X' else 'X')

    return (Player1Marker,Player2Marker)

def position_choice():
    position = 'None'
    while position not in ['1','2','3','4','5','6','7','8','9']:
        position = input("Pick a position that is unoccupied with a marker : Enter any number from 1-9 : ")
        if position not in ['1','2','3','4','5','6','7','8','9']:
            print("\n Sorry, Invalid choice")

    return position

def place_marker(Pattern, Position, marker):
    Pattern[Position] = marker


def win_check(board, mark):

    SuccessList = np.array([['1','2','3'],['4','5','6'],['7','8','9'],['1','4','7'],['2','5','8'],['3','6','9'],['1','5','9'],['3','5','7']])
    for idx in range(0,len(SuccessList)):
        if len(list(filter(lambda Index: board[Index] == mark, SuccessList[idx]))) == 3:
            print("\n Player with {} wins !!!. Congrats".format(mark))
            PlayerWon = 1
            return True

    return False

def choose_first():
    random_number = random.randint(1,2)
    Player1 = 'Player1'
    Player2 = 'Player2'
    print("\n Player 1 goes first" if random_number == 1 else "\n Player 2 goes first")
    if random_number == 1:
        return Player1
    else:
        return Player2
    

def space_check(board, position):
    default = '$'
    if board[position] == '$':
        return True
    else:
        print("\n The position you chose is occupied. Select another position")
        # Showing the above message for a couple of seconds before asking for a new position on the board
        time.sleep(3)
        return False

def full_board_check(board):
    NoDollars = 0
    for idx in range(1,len(board)+1):
        index=str(idx)
        if board[index] != '$':
            NoDollars = NoDollars + 1

    if NoDollars == 9:
        print("Board is full")
    return NoDollars

def player_choice(board):
    slot = '0'
    
    while True:
        slot = input("\n Pick a position that is unoccupied with a marker : Enter any number from 1-9")
        if slot not in ['1','2','3','4','5','6','7','8','9'] or space_check(Pattern,slot) != True:
            print("Sorry, Invalid choice")
            continue
        else:
            return slot

def replay():

    PlayAgain = 'None'
    while PlayAgain.upper() not in ['Y','N']:
        PlayAgain = input ("\n Do you wanna play again Y/N : ")
        if PlayAgain.upper() not in ['Y','N']:
            print("\n Please,Type Y or N to confirm to play")

    return PlayAgain

def RunGame(PlayerMarker, Pattern):
    PlayerPosition = position_choice()
    if space_check(Pattern,PlayerPosition) == True:
        place_marker(Pattern, PlayerPosition, PlayerMarker)
    cls()
    display_board(Pattern)

def ResetBoard():
    
    display_board(DefaultPattern)
    Prefix_player = choose_first()
    Player1Marker,Player2Marker = player_input(Prefix_player)
    return (Player1Marker,Player2Marker)
        
#------------------------------------------------------------#
print('Welcome to Tic Tac Toe! \n')

#Set up or reset the board
Player1Marker,Player2Marker = ResetBoard()
print ("\n You Chose {} and the other player will play with {}".format(Player1Marker,Player2Marker))

#Reset is set to false since this is first time setup and not reset
Reset = 'False'

while True:

    if Reset == 'True':
        cls()
        Pattern = DefaultPattern.copy()
        Player1Marker,Player2Marker = ResetBoard()
        print ("\n You Chose {} and the other player will play with {}".format(Player1Marker,Player2Marker))
        Reset = 'False'

    RunGame(Player1Marker, Pattern)
    
    if win_check(Pattern, Player1Marker) == True or win_check(Pattern, Player2Marker) == True:
        if replay() != 'Y':
            Reset = 'False'
            break
        else:
            Reset = 'True'
            continue

    NoDollars = full_board_check(Pattern)
    if NoDollars==9:
        print("\n Game Over !!! TIE Game. Well played")
        if replay() != 'Y':
            Reset = 'False'
            break
        else:
            Reset = 'True'
            continue

    RunGame(Player2Marker, Pattern)

    if win_check(Pattern, Player1Marker) == True or win_check(Pattern, Player2Marker) == True:
        if replay() != 'Y':
            Reset = 'False'
            break
        else:
            Reset = 'True'
            continue

    NoDollars = full_board_check(Pattern)
    if NoDollars==9:
        print("\n Game Over !!! TIE Game. Well played")
        if replay() != 'Y':
            Reset = 'False'
            break
        else:
            Reset = 'True'
            continue
