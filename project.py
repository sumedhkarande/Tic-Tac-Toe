def display_board(board):
    print('      |      |      ')
    print('   {}  |  {}   |  {}  '.format(board[0],board[1],board[2]))
    print('      |      |      ')
    print('--------------------')
    print('      |      |      ')
    print('  {}   |  {}   |  {}  '.format(board[3],board[4],board[5]))
    print('      |      |      ')
    print('--------------------')
    print('      |      |      ')
    print('  {}   |  {}   |  {}  '.format(board[6],board[7],board[8]))
    print('      |      |      ')


player1_input= input(" Player 1 enter either'X' OR 'O' \n")

if player1_input=='X':
    player2_input='O'
else:
    player2_input='X'
print('Player 1 is {} and Player 2 is {}'.format(player1_input,player2_input))

test_board=[' ',' ',' ',' ',' ',' ',' ',' ',' ']


def checker(Ludo):
    if (test_board[4]==test_board[3]==test_board[5]=='X' or 
        test_board[4]==test_board[1]==test_board[7]=='X' or 
        test_board[4]==test_board[2]==test_board[6]=='X' or
        test_board[4]==test_board[8]==test_board[0]=='X' or
        test_board[0]==test_board[3]==test_board[6]=='X' or
        test_board[1]==test_board[0]==test_board[2]=='X' or
        test_board[8]==test_board[2]==test_board[5]=='X' or
        test_board[6]==test_board[7]==test_board[8]=='X' or
        test_board[4]==test_board[3]==test_board[5]=='O' or 
        test_board[4]==test_board[1]==test_board[7]=='O' or 
        test_board[4]==test_board[2]==test_board[6]=='O' or
        test_board[4]==test_board[8]==test_board[0]=='O' or
        test_board[0]==test_board[3]==test_board[6]=='O' or
        test_board[1]==test_board[0]==test_board[2]=='O' or
        test_board[8]==test_board[2]==test_board[5]=='O' or
        test_board[6]==test_board[7]==test_board[8]=='O'):
        return True


def player1_game():
    player_input= int(input('Player 1, make your move from 1-9 \n'))
    test_board[player_input-1]= player1_input
def player2_game():
    player_input= int(input('Player 2, make your move from 1-9 \n'))
    test_board[player_input-1]= player2_input

game=True

while(game):
    player1_game()
    display_board(test_board)
    x=checker(test_board)
    if x==True:
        print('Player 1 Wins')
        break     
    player2_game()
    x=checker(test_board)
    if x==True:
        print('Player 2 Wins')
        break         

