# ======= A TIC TAC TOE BOARD =======

# ======= BOARD COMPONENTS SET UP USING DICTIONARY =======
board = {'T1':'T1', 'T2':'T2', 'T3':'T3',
         'M1':'M1', 'M2':'M2', 'M3':'M3',  # AN EMPTY BOARD
         'B1':'B1', 'B2':'B2', 'B3':'B3'}

# ======= A SIMPLE GRAPHICAL SET UP =======
def showBoard(board):
    print(board['T1'] + '|' + board['T2'] + '|' + board['T3']) # will grab the value in the dictionary
    print('--+--+--')
    print(board['M1'] + '|' + board['M2'] + '|' + board['M3'])
    print('--+--+--')
    print(board['B1'] + '|' + board['B2'] + '|' + board['B3'])

def winnerCheck():
    if board['T1'] == 'X' and board['T2'] == 'X' and board['T3'] == 'X':
        return True
    elif board['M1'] == 'X' and board['M2'] == 'X' and board['M3'] == 'X':
        return True
    elif board['B1'] == 'X' and board['B2'] == 'X' and board['B3'] == 'X':
        return True
    elif board['T1'] == 'X' and board['M2'] == 'X' and board['B3'] == 'X':
        return True
    elif board['T1'] == 'X' and board['M1'] == 'X' and board['B1'] == 'X':
        return True
    elif board['T2'] == 'X' and board['M2'] == 'X' and board['B2'] == 'X':
        return True
    elif board['T3'] == 'X' and board['M3'] == 'X' and board['B3'] == 'X':
        return True
    elif board['T1'] == 'O' and board['T2'] == 'O' and board['T3'] == 'O':
        return True
    elif board['M1'] == 'O' and board['M2'] == 'O' and board['M3'] == 'O':
        return True
    elif board['B1'] == 'O' and board['B2'] == 'O' and board['B3'] == 'O':
        return True
    elif board['T1'] == 'O' and board['M2'] == 'O' and board['B3'] == 'O':
        return True
    elif board['T1'] == 'O' and board['M1'] == 'O' and board['B1'] == 'O':
        return True
    elif board['T2'] == 'O' and board['M2'] == 'O' and board['B2'] == 'O':
        return True
    elif board['T3'] == 'O' and board['M3'] == 'O' and board['B3'] == 'O':
        return True
    else:
        return False

def main():
    turn = 'X'
    # === 9 TOTAL GAME PLAYS IN TTT ===
    for i in range(9):
        # === THIS INCORPORATES DICTIONARY ONTO THE SHOWBOARD ===
        showBoard(board)
        print(turn + '\'s turn. Which move? ')
        move = input()
        if move not in board:
            print('Enter a spot in the board')
            continue
        # === WILL ADD THIS VALUE IN ONTO THE KEY ===
        board[move] = turn
        if winnerCheck():
            print(turn, 'wins!')
            print("\nFinal Board:")
            showBoard(board)
            quit()

        if turn == 'X':
            turn = 'O'
        else:
            turn = 'X'

main()
print('A tie!')
print ("\nFinal Board:")
showBoard(board)