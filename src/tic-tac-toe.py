import random


def display_board(board):
    print('\n' * 100)
    print(board[7] + "  |  " + board[8] + "  |  " + board[9])
    print("______________")
    print(board[4] + "  |  " + board[5] + "  |  " + board[6])
    print("______________")
    print(board[1] + "  |  " + board[2] + "  |  " + board[3])


def player_input():
    marker = ""
    # ask player 1 if he wants X or O
    while marker != 'x' and marker != 'o':
        marker = input("player 1,choose X or O :  ")
    # assigin player the other mark
    if marker == 'x':
        marker2 = 'o'
    else:
        marker2 = 'x'

    return (marker, marker2)


def place_marker(board, markerx, position):
    board[position] = markerx


def win_check(board, mark):
    return ((board[7] == mark and board[8] == mark and board[9] == mark) or  # across the top
            (board[4] == mark and board[5] == mark and board[6] == mark) or  # across the middle
            (board[1] == mark and board[2] == mark and board[3] == mark) or  # across the bottom
            (board[7] == mark and board[4] == mark and board[1] == mark) or  # down the middle
            (board[8] == mark and board[5] == mark and board[2] == mark) or  # down the middle
            (board[9] == mark and board[6] == mark and board[3] == mark) or  # down the right side
            (board[7] == mark and board[5] == mark and board[3] == mark) or  # diagonal
            (board[9] == mark and board[5] == mark and board[1] == mark))  # diagonal


def choose_first():
    player_x = random.randint(1, 2)

    if player_x == 1:
        print('player1 goes First')
    else:
        print('player2 goes First')
    return player_x


def space_check(board, position):
    space = None
    if board[position] == " ":
        space = True
    else:
        space = False
    return (space)


def full_board_check(board):
    for n in range(1, 10):
        if space_check(board, n):
            return False
    return True


def player_choice(board):
    while True:
        try:
            x = int(input('please enter your next position'))
            if x not in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
                raise ValueError
            break
        except ValueError:
            print("invalid input")
    return (x)


def replay():
    again = input("Do you want to play again ? YES or NO :")
    if again == "yes":
        return True
    else:
        return False


def game_on():
    play_game = input('Are you ready to play? Enter Yes or No.')

    return play_game.lower()[0] == 'y'

print('Welcome to Tic Tac Toe!')

while True:
    # Set the game up here
    # pass
    board = ['', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
    player1, player2 = player_input()
    turn = choose_first()
    game = game_on()
    while game:

        if turn == 1:
            display_board(board)
            position = player_choice(board)
            space = space_check(board, position)
            while(space == False):
                position = player_choice(board)
                space = space_check(board, position)
            place_marker(board, player1, position)

            if win_check(board, player1):
                display_board(board)
                print("CONGRATULATION you won")
                game = False
            else:
                if full_board_check(board):
                    display_board(board)
                    print("It's a draw")
                    break
                else:
                    turn = 2
        else:

            display_board(board)
            position = player_choice(board)
            space = space_check(board, position)
            while (space == False):
                position = player_choice(board)
                space = space_check(board, position)
            place_marker(board, player2, position)

            if win_check(board, player2):
                display_board(board)
                print("CONGRATULATION you won")
                game = False
            else:
                if full_board_check(board):
                    display_board(board)
                    print("It's a draw")
                    break
                else:
                    turn = 1

    if not replay():
        break
