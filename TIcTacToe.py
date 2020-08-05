import random






def display_board(board):

    print(board[7] + " | " + board[8] + " | " + board[9])
    print("----------------------------------")
    print(board[4] + " | " + board[5] + " | " + board[6])
    print("----------------------------------")
    print(board[1] + " | " + board[2] + " | " + board[3])
    return 0

def player_input():
    marker = ''
    while marker != 'o' and marker != 'x':
        marker = input("Player 1 choose between o and x:")

    if marker == 'x':
        return ('x','o')
    else:
        return ('o','x')

def place_marker(board,marker,position):
    board[position] = marker

def win_check(board, mark):
    return (board[1] == mark and board[2] == mark and board[3] == mark) or \
           (board[1] == mark and board[7] == mark and board[4] == mark) or \
           (board[2] == mark and board[5] == mark and board[8] == mark) or \
           (board[3] == mark and board[6] == mark and board[9] == mark) or\
           (board[4] == mark and board[5] == mark and board[6] == mark) or \
           (board[7] == mark and board[8] == mark and board[9] == mark) or \
           (board[1] == mark and board[5] == mark and board[9] == mark) or \
           (board[3] == mark and board[5] == mark and board[7] == mark)




def choose_first():

    flip = random.randint(0,1)

    if flip == 0:
        return 'Player 1'
    else:
        return 'Player 2'



def space_check(board, position):
    return board[position] == ' '

def full_board_check(board):
    for i in range(1,10):
        if space_check(board,i):
            return False
    #Board is full if we return true
    return True



def player_choice(board):

    position = 0

    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board,position):
        position = int(input("Choose a position: (1-9)"))
    return position

def replay():

    choice = input("Play again? Enter y or n:")

    return choice == 'y'

print("Welcome to Tic Tac Toe!!!")

# while loop to game running

while True:

    #Play the game:
    the_board = [' '] * 10
    player1_marker, player2_marker = player_input()

    turn = choose_first()
    print(turn + " will go first")

    play_game = input("Ready to play? y or n")
    if play_game == 'y':
        game_on = True
    else:
        game_on = False

    while game_on:

        if turn == 'Player 1':  #Player 1 turn

            #show the board
            display_board(the_board)

            #choose a position
            position = player_choice(the_board)

            #place the marker on the position
            place_marker(the_board,player1_marker,position)

            #check if they won
            if win_check(the_board,player1_marker):
                display_board(the_board)
                print("PLAYER 1 HAS WON!!!")
                game_on = False
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print("TIE GAME!")
                    game_on = False
                else:
                    turn = 'Player 2'

        else:
            display_board(the_board)

            # choose a position
            position = player_choice(the_board)

            # place the marker on the position
            place_marker(the_board, player2_marker, position)

            # check if they won
            if win_check(the_board, player2_marker):
                display_board(the_board)
                print("PLAYER 2 HAS WON!!!")
                game_on = False
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print("TIE GAME!")
                    game_on = False
                else:
                    turn = 'Player 1'

    if not replay():
        break  # Break out of while loop on replay()
















