#Louis Le 2338697

import random
import sys
tiles = []


def tileLabels(n):
    for i in range(0, n**2 -1):
        tiles.append(i + 1)
    tiles.append(' ')
    return tiles


def getNewPuzzle(n):
    board = []
    j = 0
    tileLabels(n)
    random.shuffle(tiles)
    for i in range(n):
        row = []
        for i in range(n):
            row.append(tiles[j])
            j += 1
        board.append(row)
    return board


def findEmptyTile(board):
    i = 0
    j = 0
    for row in board:
        for number in row:
            if number == ' ':
                i = row.index(number)
                j = board.index(row)     

    return (j, i)

def nextMove(board):
    emptytile = findEmptyTile(board)
    row, column = emptytile
    while True:
        W = 'W'
        A = 'A'
        S = 'S'
        D = 'D'
        if row == 0:
            W = ''
        if row == len(board[0]) - 1:
            S = ''
        if column == 0:
            A = ''
        if column == len(board[0] ) - 1:
            D = ''
        command = input(f'Enter WASD (or QUIT): ({W}) ({A}) ({S}) ({D}) ').upper()

        if command == 'QUIT':
            sys.exit()

        if command == 'W' and W:
            board[row][column], board[row - 1][column] = board[row - 1][column], board[row][column]
            return 'W'
            
        elif command == 'A' and A:
           board[row][column], board[row][column - 1] = board[row][column - 1], board[row][column]
           return 'A'

        elif command == 'S' and S:
            board[row][column], board[row + 1][column] = board[row + 1][column], board[row][column]
            return 'S'

        elif command == 'D' and D:
           board[row][column], board[row][column + 1] = board[row][column + 1], board[row][column]
           return 'D'
        
        else:
            print('Please enter a valid move')
        
        

def displayBoard(board_lst):
    n = len(board_lst)

    labels = []
    for i in range(n):
        for j in range(n):
            labels.append(board_lst[i][j])

    draw_board = ''
    horizontal_div = ('+' + '------')*n + '+'
    vertical_div = '|' + ' '*6
    vertical_label = '|' + ' '*2 + '{}' + ' '*2
    
    for i in range(n):
        draw_board = draw_board + horizontal_div +'\n'+\
                    vertical_div*n + '|\n' + \
                    vertical_label*n + '|\n'+\
                    vertical_div*n + '|\n'
    draw_board += horizontal_div
    print(draw_board.format(*labels))



        
nextMove(getNewPuzzle(3))        
    
