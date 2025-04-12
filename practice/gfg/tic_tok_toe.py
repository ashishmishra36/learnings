# 2 players should be able to play the game (both sitting at the same computer)
# The board should be printed out every time a player makes a move
# You should be able to accept input of the player position and then place a symbol on the board

def display_game_board(board):
    print('Here is the tic toc board !!')
    print(board[1] + '   |   ' + board[2] + '   |   ' + board[3])
    print(board[4] + '   |   ' + board[5] + '   |   ' + board[6])
    print(board[7] + '   |   ' + board[8] + '   |   ' + board[9])


def clear_screen():
    print("\n" * 100)


def player_input():
    choice = ''
    acceptable_values = ('X', 'O')
    while choice not in acceptable_values:
        choice = input('Enter a value from X or O : ')
        if choice not in acceptable_values:
            print('Sorry Please enter any of the values X or O ! ')
        player_one = choice
        if player_one == 'X':
            player_two = 'O'
        else:
            player_two = 'X'
    return player_one, player_two


def place_marker(board, marker):
    position = ''
    while position not in range(1, 10):
        position = int(input('Type 1...9 to place to a position : '))
        if position not in range(1, 10):
            print('Please enter any position in range of 1-9')
        else:
            if not space_check(board, position):
                print('Selected position is not FREE ! Please choose a different position !')
                position = 'invalid'
    board[position] = marker
    return board

#function that returns True if the given mark has won
def win_check(board, mark):
    list_win_tuples = [(1, 2, 3), (1, 4, 7), (1, 5, 9), (2, 5, 8), (3, 6, 9), (3, 5, 7)]
    for items in list_win_tuples:
        if board[items[0]] == board[items[1]] == board[items[2]] == mark:
            return True


#function that returns True the given space on the board is free
def space_check(board, position):
    return board[position] not in ('X', 'O')


# returns true if board is full
def full_board_check(board):
    return '' not in board


def replay():
    clear_screen()
    choice = ''
    acceptable_values = ('Y', 'N')
    while choice not in acceptable_values:
        choice = input('You want to replay say Y - Yes and N for No : ')
        if choice not in acceptable_values:
            print('Sorry Please enter any of the values Y or N! ')
        if choice == 'N':
            print('Game is Finished !!')
    return choice == 'Y'


def lets_play():
    print('*******************Welcome to Tic Tac Toe!*******************')
    re_play = True
    while re_play:
        board = ['', '', '', '', '', '', '', '', '', '']

        display_game_board(board)

        player_one, player_two = player_input()
        print(f'Player-1 has a marker {player_one} & Player-2 has a marker {player_two}')

        for attempt in range(0, 9):
            if attempt % 2 == 0:
                player_name = 'player_one'
                marker = player_one
            else:
                player_name = 'player_two'
                marker = player_two
            print('--------------------------------------------------')
            print(f'Its turn for {player_name} :::')
            board = place_marker(board, marker)

            display_game_board(board)

            if win_check(board, marker):
                print(f'Game is over!! {player_name} is won')
                break
            if not win_check(board, marker) and attempt ==8:
                print('Oops ! Nobody won ! Its a tie')


        re_play = replay()


# # start playing the game
lets_play()
# board = ['qwe', 'X', 'O', 'X', 'O', 'X', 'O', 'X', 'O', 'X']
# mark ='X'
# win_check(board, mark)