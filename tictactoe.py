import random
#***************TIC TAC TOE GAME***************
# REQUIREMENTS
# - The game is played by 2 players sitting at the same computer
# - The board should be displayed everytime a player makes a move
# - User input of marker position should be accepted and then the marker is placed on the board

# FUNCTION TO DISPLAY THE TICTACTOE BOARD
def display_board(board):
    print('   |   |   ')
    print(' '+board[7]+' |'+' '+board[8]+' |'+' '+board[9]+' ')
    print('   |   |   ')
    print('___________')
    print('   |   |   ')
    print(' '+board[4]+' |'+' '+board[5]+' |'+' '+board[6]+' ')
    print('   |   |   ')
    print('___________')
    print('   |   |   ')
    print(' '+board[1]+' |'+' '+board[2]+' |'+' '+board[3]+' ')
    print('   |   |   ')


# FUNCTION TO TAKE IN A PLAYER INPUT AND ASSIGN THEIR MARKER AS 'X' OR 'O'
def player_input():
    marker = ''
    while not (marker=='X' or marker=='O'):
        marker=input('Do you want to be X or O?').upper()

    if marker == 'X':
        return ('X','O')
    else:
        return ('O','X')


# FUNCTION TO TAKE IN THE BOARD LIST, A MARKER, AND PREFERRED POSITION.
# THEN ASSIGN IT TO THE BOARD
def place_marker(board,marker,position):
    board[position]=marker


# FUNCTION TO ASK A PLAYER WHERE TO PUT THEIR SELECTED MARKER
def select_position(board):
    position=0
    while position not in [1,2,3,4,5,6,7,8,9] or not space_checker(board, position):
        position=int(input('Where do you want to put your marker?: '))

    return position


# FUNCTION TO CHECK WHETHER A PLAYER WINS
def win_checker (board,mark):
    if board[1]==mark and board[2]==mark and board[3]==mark:
        return True
    elif board[4]==mark and board[5]==mark and board[6]==mark:
        return True
    elif board[7]==mark and board[8]==mark and board[9]==mark:
        return True
    elif board[1]==mark and board[4]==mark and board[7]==mark:
        return True
    elif board[2]==mark and board[5]==mark and board[8]==mark:
        return True
    elif board[3]==mark and board[6]==mark and board[9]==mark:
        return True
    elif board[1]==mark and board[5]==mark and board[9]==mark:
        return True
    elif board[3]==mark and board[5]==mark and board[7]==mark:
        return True
    else:
        pass


# FUNCTION TO CHECK WHETHER THE SPACE IS AVAILABLE
def space_checker(board,position):
    if board[position]==' ':
        return True
    else:
        return False


# FUNCTION TO CHECK WHETHER THE BOARD IS FULL
def full_board_checker(board):
    for idx in range(1,len(board)):
        if space_checker(board, idx):
            return False
    return True


# FUNCTION TO DETERMINE WHO GOES FIRST
def choose_first():
    if random.randint(0, 1) == 0:
        return 'Player 2'
    else:
        return 'Player 1'


# FUNCTION TO REPLAY THE GAME
def replay():
    userinput=input('Do you want to play again? Enter Yes or No: ').lower()
    if userinput[0]=='y':
        return True
    return False

# FUNCTION TO PLAY THE GAME
def play_game():
    print('WELCOME TO TIC TAC TOE')
    theBoard=[' ']*10
    player1_marker, player2_marker = player_input()
    turn = choose_first()
    print(turn+' will go first.')

    start_play = input('Are you ready? Enter y or n: ')
    if start_play == 'y':
        game_on=True
    else:
        game_on=False

    while game_on:
        if turn=='Player 1':
            display_board(theBoard)
            print('Player 1 turn')
            position=select_position(theBoard)
            place_marker(theBoard, player1_marker, position)

            if win_checker(theBoard,player1_marker):
                display_board(theBoard)
                print('You win!')
                game_on=False
                if replay():
                    game_on=True
            else:
                if full_board_checker(theBoard):
                    display_board(theBoard)
                    print('Draw!')
                    game_on=False
                    if replay():
                        game_on=True
                else:
                    turn = 'Player 2'

        else:
            display_board(theBoard)
            print('Player 2 turn')
            position=select_position(theBoard)
            place_marker(theBoard, player2_marker, position)

            if win_checker(theBoard,player2_marker):
                display_board(theBoard)
                print('You win!')
                game_on=False
                if replay():
                    game_on=True
            else:
                if full_board_checker(theBoard):
                    display_board(theBoard)
                    print('Draw!')
                    game_on=False
                    if replay():
                        game_on=True
                else:
                    turn = 'Player 1'



play_game()
